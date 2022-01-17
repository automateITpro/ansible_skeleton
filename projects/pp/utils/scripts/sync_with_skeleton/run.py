#!/usr/bin/env python3

import questionary
import re
import os
import shutil
from pathlib import Path
from git import Repo
import yaml

BASE_PATH = Path(os.path.dirname(os.path.realpath(__file__)))
print ("Syncing with skeleton...")

PLAYBOOKS_PATH = Path(BASE_PATH, "playbooks")
ROLES_PATH = Path(BASE_PATH, "roles")
UTILS_PATH = Path(BASE_PATH, "utils")
UTIL_PATH = Path(UTILS_PATH, "scripts", "sync_with_skeleton")
SETTINGS_FILE = Path(UTIL_PATH, "settings", "settings.yml")
TEMP_PATH = Path(UTILS_PATH, "tmp", "sync_with_skeleton")
TEMP_REPO_PATH = Path(TEMP_PATH, "repo")
SSH_KEYS_PATH = Path(Path.home(), ".ssh")
# SKELETON_PATH = Path(TEMP_REPO_PATH, "utils", "assets", "project_skeleton", "aws")


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

repo = Repo(search_parent_directories = True)
if Path.exists(PLAYBOOKS_PATH):
  shutil.rmtree(PLAYBOOKS_PATH)
if Path.exists(ROLES_PATH):
  shutil.rmtree(ROLES_PATH)
if not TEMP_REPO_PATH.exists():
  repo = Repo(search_parent_directories = True).clone_from(
      "git@bitbucket.org:zenitech/infra-ansible.git",
      TEMP_REPO_PATH,
      branch = "skeleton",
      env = {
        "GIT_SSH_COMMAND": "ssh -i %s" % (ssh_key)
      }
    )
else:
  repo = Repo(TEMP_REPO_PATH)
  repo.head.reset(index = True, working_tree = True)
  repo.git.clean("-xdf")
  repo.heads.skeleton.checkout()
  repo.remotes.origin.pull(env = { "GIT_SSH_COMMAND": "ssh -i %s" % (ssh_key) })
shutil.copytree(Path(TEMP_REPO_PATH, "utils/assets/project_skeleton/playbooks"), PLAYBOOKS_PATH, symlinks = True)
shutil.copytree(Path(TEMP_REPO_PATH, "utils/assets/project_skeleton/roles"), ROLES_PATH, symlinks = True)