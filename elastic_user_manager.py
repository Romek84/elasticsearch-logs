from elasticsearch import Elasticsearch

# Connecting to Elasticsearch
def connect_to_elasticsearch(password):
    es = Elasticsearch(
        [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
        basic_auth=("elastic", password)
    )
    return es

# Retrieving the list of users
def get_users(es):
    users = es.security.get_user()
    for username, user_info in users.items():
        print(f"Username: {username}, Full Name: {user_info.get('full_name')}, Roles: {user_info.get('roles')}")

# Creating a new user
def create_user(es, username, password, roles, full_name=None):
    es.security.put_user(
        username=username,
        body={
            "password": password,
            "roles": roles,
            "full_name": full_name
        }
    )
    print(f"User {username} has been created")

# Deleting a user
def delete_user(es, username):
    es.security.delete_user(username=username)
    print(f"User {username} has been deleted")

# Updating a user's password and roles
def update_user(es, username, new_password=None, new_roles=None):
    body = {}
    if new_password:
        body["password"] = new_password
    if new_roles:
        body["roles"] = new_roles
    es.security.put_user(username=username, body=body)
    print(f"User data for {username} has been updated")

# Filtering users by role
def filter_users_by_role(es, role):
    users = es.security.get_user()
    print(f"\nUsers with the role '{role}':")
    for username, user_info in users.items():
        if role in user_info.get('roles', []):
            print(f"Username: {username}, Full Name: {user_info.get('full_name')}, Roles: {user_info.get('roles')}")

# Retrieving available roles
def get_available_roles():
    return ["superuser", "kibana_system", "logstash_system", "beats_system", "apm_system", "remote_monitoring_user"]

# Main function
if __name__ == "__main__":
    password = input("Enter the password for Elasticsearch: ")
    es = connect_to_elasticsearch(password)
    print("Connected to Elasticsearch")

    while True:
        print("\nSelect an option:")
        print("1. Get the list of users")
        print("2. Create a new user")
        print("3. Update a user")
        print("4. Delete a user")
        print("5. Filter users by role")
        print("6. Exit")

        option = input("Enter the option number: ")

        if option == '1':
            get_users(es)
        elif option == '2':
            username = input("Enter the username: ")
            password = input("Enter the password: ")

            # Role selection
            available_roles = get_available_roles()
            print("Available roles:")
            for i, role in enumerate(available_roles, 1):
                print(f"{i}. {role}")
            role_choice = int(input("Select the role number (or enter multiple separated by commas): "))

            if 1 <= role_choice <= len(available_roles):
                roles = [available_roles[role_choice - 1]]
            else:
                # The user can enter multiple roles
                roles = input("Enter roles (separated by commas): ").split(",")
                roles = [role.strip() for role in roles if role.strip()]  # Remove empty roles

            full_name = input("Enter the full name (or leave blank): ")
            create_user(es, username, password, roles, full_name)
        elif option == '3':
            username = input("Enter the username to update: ")
            new_password = input("Enter the new password (or leave blank): ")
            new_roles = input("Enter new roles (separated by commas, or leave blank): ").split(",")
            new_roles = [role.strip() for role in new_roles if role.strip()]  # Remove empty roles
            update_user(es, username, new_password if new_password else None, new_roles if new_roles else None)
        elif option == '4':
            username = input("Enter the username to delete: ")
            delete_user(es, username)
        elif option == '5':
            available_roles = get_available_roles()
            print("Available roles:")
            for i, role in enumerate(available_roles, 1):
                print(f"{i}. {role}")
            role_choice = int(input("Select the role number to filter: ")) - 1

            if 0 <= role_choice < len(available_roles):
                selected_role = available_roles[role_choice]
                filter_users_by_role(es, selected_role)
            else:
                print("Invalid role selection.")
        elif option == '6':
            print("Program terminated.")
            break
        else:
            print("Invalid option. Try again.")
