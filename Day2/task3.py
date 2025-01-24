# 3-Write a script that checks if a given port number is valid (valid ports are between 0 and 65535). Print True if valid, otherwise False.


port = int(input("Enter a port number: "))

if (port >= 0 and port <= 65535):
    print(f"Port {port} is valid")
else:
    print(f"Port {port} is not valid")
