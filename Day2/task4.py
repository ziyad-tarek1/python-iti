
# 4-Simulate a login system:

# 	Ask the user to input a username and password.

# 	Check if the username is "admin" and the password is "admin123".

# 	Print "Access granted" if both are correct, otherwise print "Access denied".

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    print("Access granted")
else:
    print("Access denied")
