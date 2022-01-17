# README #

Ansible script:  **#{project_name}** 

### Description ###

Here we consolidate our CaaC infrastructure components for project **#{project_name}**.

### Project structure ###

```
inventories/
   main/
      hosts.yml               # inventory file for production servers
      group_vars/
         group1.yml       # here we assign variables to particular groups
         group2.yml
      host_vars/
         hostname1.yml    # here we assign variables to particular systems
         hostname2.yml

library/                  # if any custom modules, put them here (optional) 
module_utils/             # if any custom module_utils to support modules, put them here (optional)
filter_plugins/           # if any custom filter plugins, put them here (optional)

site.yml                  # Main playbook

roles/                    # Hierrarchy of roles
README.md                 # Documentation of a project
```

### Variables used ###

#### Group variables ####

| Name | Type | Default value | Description  |
|---|---|---|---|

#### Host variables ####

| Name | Type | Default value | Description  |
|---|---|---|---|

### Hosts ###

| Name | Address | Connection type | Description  |
|---|---|---|---|

### Modules ###

| Name | Type | Default value | Description  |
|---|---|---|---|

### Usage example ###

```ansible-playbook -i inventories/production/hosts.yml site.yml```

### Who do I talk to ###

[#{author_name}](mailto:#{author_email})