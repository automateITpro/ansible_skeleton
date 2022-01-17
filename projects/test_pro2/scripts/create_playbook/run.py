import os
from pathlib import Path
from posixpath import join
import questionary

def create_role(location, author_name, author_email, playbook_name):
    dirs_to_create = [
        os.path.join(location),
        os.path.join(location, playbook_name),
        os.path.join(location, playbook_name, "files"),
    ]
    files_to_create = [
        os.path.join(location, playbook_name, "main.yml"),
        os.path.join(location, playbook_name, "README.md")
    ]

    # Create the role skeleton
    print("Creating role directories")
    for d in dirs_to_create:
        Path(d).mkdir(parents=True, exist_ok=True)

    print("Creating role files")
    for f in files_to_create:
        open(f, 'a').close()

    readme_file = open(Path(BASE_PATH, 'templates', 'playbook','README.md'), 'r').read()
    readme_file = readme_file.replace('#{playbook_name}', playbook_name)
    readme_file = readme_file.replace('#{author_name}', author_name)
    readme_file = readme_file.replace('#{author_email}', author_email)
    open(Path(location, playbook_name, 'README.md'), 'w').write(readme_file)

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

author_name = questionary.text("Please input your full name").ask()
author_email = questionary.text("Please input your email").ask()

playbook_location = Path(BASE_PATH, "playbooks")
playbooks_to_create = questionary.text("What playbooks to create? Insert names with spaces").ask()
playbooks_to_create = playbooks_to_create.split( )

path = questionary.path("Insert playbook location. Default location: project_dir/playbooks?").ask()
if len(path) <= 0:
    path = playbook_location

for r in playbooks_to_create:
    print("Creating playbooks: ", r)
    create_role(path, author_name, author_email, r)