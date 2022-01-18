# README 

Role:  **shell_command** 

### Description

This role is responsible for running shell commands on remote host.

### Role structure

```
/files            # files needed for role       
/handlers         # handlers for the role
/tasks            # tasks to be executed by the role
/templates        # templates which can be deployed via this role.
/vars             # variables for the role
/defaults         # default variables of role

README.md         # Documentation of a role
```

### Variables used

| Name         | Type                               | Default value | Description                                    |
|--------------|------------------------------------|---------------|------------------------------------------------|
| **commands** | *list(object(command, directory))* | *none*        | List of commands and directories for execution |

### Handlers used 

| Name | Description |
|------|-------------|

### Example use

---
  roles:
    - role: '/path/to/my/roles/shell_command'

### Who do I talk to 

[Paulius Gasparavicius](mailto:paulius.gasparavicius@zenitech.co.uk)