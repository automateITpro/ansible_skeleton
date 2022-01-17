#!/usr/bin/env python3
import os
from pathlib import Path
from git import Repo
import questionary

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPTS_PATH = Path(BASE_PATH, 'scripts')

scripts = (entry for entry in os.scandir(SCRIPTS_PATH) if entry.is_dir())
menu = questionary.select("Select item", [script.name for script in scripts]).ask()
exec(open(Path(SCRIPTS_PATH, menu, 'run.py')).read())