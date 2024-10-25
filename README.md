Elastic _user_manager:

This script allows for efficient management of user accounts in an Elasticsearch environment, with functionalities including connecting to an Elasticsearch instance, retrieving user lists, creating new users, updating user credentials and roles, deleting users, and filtering users by specific roles. Each function is modularized to focus on different user management tasks, making it suitable for both individual account management and broader administrative purposes.

Main functionalities:
Connecting to Elasticsearch: Establishes a secure connection using basic_auth credentials.
Getting User List: Retrieves a list of all users, displaying usernames, full names, and assigned roles.
Creating a New User: Adds new user accounts with specified passwords, roles, and optional full names.
Updating User Information: Modifies existing users’ passwords and roles.
Deleting Users: Removes specified user accounts.
Filtering Users by Role: Lists users who have a specific role.
Available Roles: Provides a predefined set of roles, including "superuser," "kibana_system," and others.
Interactive Menu:
The script includes a command-line menu, prompting for different user management actions. Each option is explained and enables the user to create, update, filter, and delete users in an interactive manner.

This setup is ideal for administrators working within Elasticsearch who want to streamline their user management workflows.
