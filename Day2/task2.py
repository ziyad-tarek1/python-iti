# 2-Write a script that takes a server hostname (e.g., "web-server-01") and extracts the numeric part (01) from the string. Print the extracted number as an integer.


hostname = input("Enter server hostname (ex: 'web-server-01'): ")
numeric_part = ''.join(filter(str.isdigit, hostname))
if numeric_part:
    print(f"The extracted number is: {int(numeric_part)}")
else:
    print("No numeric part found in the hostname.")
