
import os

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
    return content

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File '{file_path}' has been written successfully.")

def append_file(file_path, content):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found. Cannot append.")
        return
    with open(file_path, 'a') as file:
        file.write(content)
    print(f"Content has been appended to the file '{file_path}'.")

# Function to read and write to a file at the same time
def read_and_write_file(file_path, content):

    # Open the file in read-write mode ('r+')
    with open(file_path, 'r+') as file:
        # Read the existing content
        existing_content = file.read()
        print("Existing content:")
        print(existing_content)
        
        # Write new content to the file
        file.seek(len(read_file(file_path)))  # Move the cursor to the end of the file
        file.write(content)
        
        # Read the updated content
        file.seek(0)  # Move the cursor to the beginning again
        updated_content = file.read()
        print("Updated content:")
        print(updated_content)
    
    return updated_content  # Return the updated content for further use
