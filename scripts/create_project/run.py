#!/usr/bin/env python3
import questionary
import re
import os
import shutil
from pathlib import Path


BASE_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECTS_PATH = Path(BASE_PATH, 'projects')
TEMPLATES_PATH = Path(BASE_PATH, 'templates')
PROJECT_SKELETON_PATH = Path(TEMPLATES_PATH, 'project')
ROLES_PATH = Path(BASE_PATH, 'roles')
PLAYBOOKS_PATH = Path(BASE_PATH, 'playbooks')

project_name = questionary.path("Please input project name").ask()
author_name = questionary.text("Please input your full name").ask()
author_email = questionary.text("Please input your email").ask()

PROJECT_PATH = Path(PROJECTS_PATH, project_name)

if PROJECT_PATH.exists():
  shutil.rmtree(PROJECT_PATH)

print("Creating project...")
shutil.copytree(PROJECT_SKELETON_PATH, PROJECT_PATH, symlinks = True)
shutil.copytree(ROLES_PATH, Path(PROJECT_PATH, 'roles'), symlinks = True)
shutil.copytree(PLAYBOOKS_PATH, Path(PROJECT_PATH, 'playbooks'), symlinks = True)


readme_file = open(Path(TEMPLATES_PATH,'README.md'), 'r').read()
readme_file = readme_file.replace('#{project_name}', project_name)
readme_file = readme_file.replace('#{author_name}', author_name)
readme_file = readme_file.replace('#{author_email}', author_email)
open(Path(PROJECT_PATH, 'README.md'), 'w').write(readme_file)
