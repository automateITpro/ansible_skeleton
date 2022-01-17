import os
from pathlib import Path
from posixpath import join
import questionary

def create_role(location, author_name, author_email, rolename):
    dirs_to_create = [
        os.path.join(location),
        os.path.join(location, rolename),
        os.path.join(location, rolename, "tasks"),
        os.path.join(location, rolename, "handlers"),
        os.path.join(location, rolename, "templates"),
        os.path.join(location, rolename, "files"),
        os.path.join(location, rolename, "vars")
    ]
    files_to_create = [
        os.path.join(location, rolename, "files", ".gitkeep"),
        os.path.join(location, rolename, "templates", ".gitkeep"),
        os.path.join(location, rolename, "vars", ".gitkeep"),
        os.path.join(location, rolename, "tasks", "main.yml"),
        os.path.join(location, rolename, "handlers", "main.yml"),
        os.path.join(location, rolename, "README.md")
    ]

    # Create the role skeleton
    print("Creating role directories")
    for d in dirs_to_create:
        Path(d).mkdir(parents=True, exist_ok=True)

    print("Creating role files")
    for f in files_to_create:
        open(f, 'a').close()

    readme_file = open(Path(BASE_PATH, 'templates', 'role','README.md'), 'r').read()
    readme_file = readme_file.replace('#{role_name}', rolename)
    readme_file = readme_file.replace('#{author_name}', author_name)
    readme_file = readme_file.replace('#{author_email}', author_email)
    open(Path(location, rolename, 'README.md'), 'w').write(readme_file)

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

author_name = questionary.text("Please input your full name").ask()
author_email = questionary.text("Please input your email").ask()

role_location = Path(BASE_PATH, "roles")
roles_to_create = questionary.text("What roles to create? Insert names with spaces").ask()
roles_to_create = roles_to_create.split( )

path = questionary.path("Insert role location. Default location: project_dir/roles?").ask()
if len(path) <= 0:
    path = role_location

for r in roles_to_create:
    print("Creating role: ", r)
    create_role(path, author_name, author_email, r)