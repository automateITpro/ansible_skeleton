# README #

Role:  **#{role_name}** 

### Description ###

Here we consolidate our CaaC infrastructure components for role **#{role_name}**.

### Role structure ###

```
/files            # files needed for role       
/handlers         # handlers for the role
/tasks            # tasks to be executed by the role
/templates        # templates which can be deployed via this role.
/vars             # variables for the role

README.md         # Documentation of a role
```

### Variables used ###

#### Variables ####

| Name | Type | Description  |
|---|---|---|

#### Files ####

| Name | Description  |
|---|---|

### Handlers ###

| Name | Description  |
|---|---|

### Templates ###

| Name | Description  |
|---|---|


### Example of how to call a role in a playbook ###

---
  roles:
    - role: '../../roles/#{role_name}'



### Who do I talk to ###

[#{author_name}](mailto:#{author_email})