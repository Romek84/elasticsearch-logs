1. elasticsearch_user_management.py
This script allows for creating, updating, deleting, and filtering users within an Elasticsearch environment.

Key Functionalities:
Connecting to Elasticsearch: Prompts the user for the Elasticsearch password, using basic authentication for secure access.
User Management:
Retrieve Users: Lists all existing users with their full name and assigned roles.
Create User: Adds a new user with specified roles and optional full name.
Update User: Updates user roles and password.
Delete User: Removes a specified user from Elasticsearch.
Filter by Role: Filters and displays users based on their assigned role.
Available Roles: Lists available roles for easier user role assignment.


2. elasticsearch_index_and_document_management.py
This script helps with index management and document insertion in Elasticsearch, aimed at creating an index, adding sample documents, and querying them.

Key Functionalities:
Connecting to Elasticsearch: Establishes a connection and verifies it.
Index Management:
Check Index Existence: Verifies if a specified index (log-index) exists; if not, it creates the index.
Document Management:
Add Sample Documents: Inserts sample documents with author names, text, and timestamps, allowing for easy testing of the index.
Query Execution: Runs a basic match_all query to retrieve and display all documents within the index.
