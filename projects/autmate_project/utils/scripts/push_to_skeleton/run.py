#!/usr/bin/env python3

import os
import shutil
from pathlib import Path
import hcl2
import yaml
from git import Repo
import questionary
import re
import sys
import platform

def getMaxFileNameLength(file_path):
  MAX_EXTENSION_LENGTH = 10 #Reserving 10 characters for git .lock file extension
  if platform.system() == "Windows":
    file_name_length = "255"
  else:
    file_name_length = os.pathconf(file_path, "PC_NAME_MAX")  
  return file_name_length - MAX_EXTENSION_LENGTH
  
BASE_PATH = Path(os.path.dirname(os.path.realpath(__file__)))
PLAYBOOKS_PATH = Path(BASE_PATH, "playbooks")
ROLES_PATH = Path(BASE_PATH, "roles")
UTILS_PATH = Path(BASE_PATH, "utils")
UTIL_PATH = Path(UTILS_PATH, "scripts", "push_to_skeleton")
SETTINGS_FILE = Path(UTIL_PATH, "settings", "settings.yml")
TEMP_PATH = Path(UTILS_PATH, "tmp", "push_to_skeleton")
TEMP_REPO_PATH = Path(TEMP_PATH, "repo")
SSH_KEYS_PATH = Path(Path.home(), ".ssh")
# SKELETON_PATH = Path(TEMP_REPO_PATH, "utils", "assets", "project_skeleton", "aws")
# modules_to_upload = input({
#   'type': 'checkbox',
#   'message': 'Please select module(s) to upload:',
#   'choices': [
#     { 'name': str(item.relative_to(MODULES_PATH)) } for item in sorted(MODULES_PATH.glob('**'))
#       if item.is_dir() and Path(item, 'README.md').is_file()
#   ],
# })
choices = []
for item in sorted(PLAYBOOKS_PATH.glob('*')):
  if item.is_dir() and Path(item, 'README.md').is_file():
    choices.append(str(item.relative_to(PLAYBOOKS_PATH)))
  elif item.is_dir() and not Path(item, 'README.md').is_file():
    print("README.md is missing in:, ",item.relative_to(PLAYBOOKS_PATH))


if len(choices) > 0:
  playbooks_to_upload = questionary.checkbox(
      "Please select playbooks to upload:", choices).ask()
else:
  playbooks_to_upload = []

choices = []
for item in sorted(ROLES_PATH.glob('*')):
  if item.is_dir() and Path(item, 'README.md').is_file():
    choices.append(str(item.relative_to(ROLES_PATH)))
  elif item.is_dir() and not Path(item, 'README.md').is_file():
    print("README.md is missing in:, ",item.relative_to(ROLES_PATH))

if len(choices) > 0:
  roles_to_upload = questionary.checkbox(
      "Please select roles to upload:", choices).ask()
else:
  roles_to_upload = []


if len(playbooks_to_upload) == 0 and len(roles_to_upload) == 0:
  print('No modules have been selected.')
  sys.exit()

if not SETTINGS_FILE.exists():
  ssh_key = questionary.select("Select item", [
      str(item) for item in sorted(SSH_KEYS_PATH.iterdir())
        if item.is_file() and Path(SSH_KEYS_PATH, "%s.pub" % (item)).is_file()
    ]).ask()  
  with open(SETTINGS_FILE.resolve(), "w") as settings_file:
    yaml.dump({ "ssh_key": ssh_key }, settings_file)
else:
  with open(SETTINGS_FILE.resolve()) as settings_file:
    ssh_key = yaml.full_load(settings_file)["ssh_key"]


if not TEMP_REPO_PATH.exists():
  repo = Repo(search_parent_directories = True).clone_from(
      "git@bitbucket.org:zenitech/infra-ansible.git",
      TEMP_REPO_PATH,
      branch = "master",
      depth = 1,
      env = {
        "GIT_SSH_COMMAND": "ssh -i %s" % (ssh_key)
      }
    )
else:
  repo = Repo(TEMP_REPO_PATH)

branch_name = re.sub(r'[^a-z0-9]', '-', '%s_%s' % (repo.config_reader().get_value('user', 'name').lower(), '-'.join(roles_to_upload + playbooks_to_upload).lower()))[ 0: getMaxFileNameLength(TEMP_REPO_PATH) ]

repo.head.reset(index = True, working_tree = True)
repo.git.clean('-xdf')
repo.heads.master.checkout()
repo.remotes.origin.pull(env = { "GIT_SSH_COMMAND": 'ssh -i %s' % (ssh_key) })

try:
  repo.heads[branch_name].checkout()
except:
  head = repo.create_head(branch_name)
  head.checkout()
repo.remotes.origin.pull(env = { "GIT_SSH_COMMAND": 'ssh -i %s' % (ssh_key) })

for module_name in playbooks_to_upload:
  print(module_name)
  shutil.rmtree(Path(TEMP_REPO_PATH, 'playbooks', module_name), ignore_errors = True)
  shutil.copytree(Path(PLAYBOOKS_PATH, module_name), Path(TEMP_REPO_PATH, 'playbooks', module_name), symlinks = True)

for module_name in roles_to_upload:
  print(module_name)
  shutil.rmtree(Path(TEMP_REPO_PATH, 'roles', module_name), ignore_errors = True)
  shutil.copytree(Path(ROLES_PATH, module_name), Path(TEMP_REPO_PATH, 'roles', module_name), symlinks = True)

repo.git.add('-A')
try:
  repo.git.commit('-m', 'Module updates')
except:
  pass
repo.git.push('-u', 'origin', branch_name, env = { "GIT_SSH_COMMAND": 'ssh -i %s' % (ssh_key) })

repo.head.reset(index = True, working_tree = True)
repo.git.clean('-xdf')
repo.heads.master.checkout()
repo.remotes.origin.pull(env = { "GIT_SSH_COMMAND": 'ssh -i %s' % (ssh_key) })