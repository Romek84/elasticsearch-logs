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


2. index_logs.py
   
This script connects to an Elasticsearch instance, checks for a specified index, and performs indexing and querying operations with pagination.

Key Functionalities:
Connecting to Elasticsearch: Connects securely to an Elasticsearch instance using basic authentication.
Index Management:
Index Check & Creation: Checks if a specified index exists; if not, creates the index.
Sample Data Insertion: Adds a set of sample documents with author, text, and timestamp fields for testing purposes.
Data Query with Pagination:
Allows querying all documents within the index using pagination parameters (page and page_size) for efficient data retrieval.
Displays the total number of results and lists document details for the current page.
