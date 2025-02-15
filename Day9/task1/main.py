
import subprocess
import sys

def show_users():
    print("Listing all users (excluding system users):")
    try:
        result = subprocess.run(["awk", "-F:", "$3 >= 1000 && $1 != \"nobody\" {print $1}", "/etc/passwd"], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")


def show_groups():
    print("Listing all groups (excluding system groups):")
    try:
        
        result = subprocess.run(["awk", "-F:", "$3 >= 1000 {print $1}", "/etc/group"], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")


def create_user():
    username = input("Enter the username to create: ")
    try:
        
        subprocess.run(["id", username], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"User {username} already exists.")
    except subprocess.CalledProcessError:
       
        subprocess.run(["sudo", "useradd", username], check=True)
        print(f"User {username} created successfully.")


def delete_user():
    username = input("Enter the username to delete: ")
    try:
        
        subprocess.run(["id", username], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        subprocess.run(["sudo", "userdel", "-r", username], check=True)
        print(f"User {username} deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"User {username} does not exist.")

def change_password():
    username = input("Enter the username to change password: ")
    try:
        subprocess.run(["id", username], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["sudo", "passwd", username], check=True)
    except subprocess.CalledProcessError:
        print(f"User {username} does not exist.")

def create_group():
    groupname = input("Enter the group name to create: ")
    try:
        subprocess.run(["getent", "group", groupname], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Group {groupname} already exists.")
    except subprocess.CalledProcessError:
        subprocess.run(["sudo", "groupadd", groupname], check=True)
        print(f"Group {groupname} created successfully.")

def delete_group():
    groupname = input("Enter the group name to delete: ")
    try:
        subprocess.run(["getent", "group", groupname], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["sudo", "groupdel", groupname], check=True)
        print(f"Group {groupname} deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Group {groupname} does not exist.")

def change_file_permissions():
    filepath = input("Enter the full path to the file (as: /the/path/you/want/to/change/permissions): ")
    try:
        subprocess.run(["sudo", "test", "-e", filepath], check=True)
        perms = input("Enter the new permissions (e.g., 755): ")
        subprocess.run(["sudo", "chmod", perms, filepath], check=True)
        print(f"Permissions for {filepath} changed to {perms}.")
    except subprocess.CalledProcessError:
        print(f"File {filepath} does not exist.")

def main():
    while True:
        print("\nAdministration Script")
        print("1. Show all users")
        print("2. Show all groups")
        print("3. Create a new user")
        print("4. Delete a user")
        print("5. Change user password")
        print("6. Create a new group")
        print("7. Delete a group")
        print("8. Change file permissions")
        print("9. Exit")
        choice = input("Select an option (1-9): ")

        if choice == "1":
            show_users()
        elif choice == "2":
            show_groups()
        elif choice == "3":
            create_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            change_password()
        elif choice == "6":
            create_group()
        elif choice == "7":
            delete_group()
        elif choice == "8":
            change_file_permissions()
        elif choice == "9":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
