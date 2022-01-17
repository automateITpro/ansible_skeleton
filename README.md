# README #

Configuration as a Code

### What is this repository for? ###

Here we consolidate our Ansible roles and playbooks for a dynamic infrastructure.

### How do I get set up? ###

1. Install [Python](https://www.python.org/downloads/source/)
1. Install [PIP](https://pip.pypa.io/en/stable/installing/)
1. Install [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
1. Run the following code and install all dependencies:
    ```shell
    pip install -r requirements.txt
    ```
1. Run the following script and complete interactive process of a project creation:
    ```shell
    ./run.py
    ```
1. Your project is created under **projects** directory. Copy it to your specific repository.
1. Read the README.md file from your project base directory for further instructions.

### Present roles ###

### How do I execute playbooks? ###
* Execute ansible playbooks by simply executing command i.e.:   
`ansible-playbook playbooks/some_playbook.yml -i inventories/main/hosts.yml -k`

* `ansible-playbook` invokes the ansible executable
* `playbooks/some_playbook.yml` defines the playbook and its path to it
* `-i` parameter defines the machine on which the playbook will be executed for example:       
`-i inventories/main/hosts.yml`   

`-k` parameter is used for asking SSH password instead of using ssh key-pair. Keep in mind that you need to install sshpass prior to executing playbook(s).
Install sshpass with: `sudo apt install sshpass`

### Who do I talk to? ###

[Paulius Gasparavicius](mailto:paulius.gasparavicius@zenitech.co.uk)
[Kintautas Puodziukynas](mailto:kintautas.puodziukynas@zenitech.co.uk)