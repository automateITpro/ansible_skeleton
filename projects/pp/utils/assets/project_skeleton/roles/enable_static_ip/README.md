# README #

Role:  **enable_static_ip** 

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

example_var: example_value

### Example of how to call a role in a playbook ###

---
  roles:
    - role: '/path/to/my/roles/#{role_name}'



### Who do I talk to ###

[#{author_name}](mailto:#{author_email})