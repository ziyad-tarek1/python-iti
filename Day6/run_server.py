# Task 1 Day 6
# create a class called server 
# attributes number *choosen by you *
# methods number *choosen by you *
# inside the server class create a class count must be exist
# create three objects


from server import Server

server1 = Server("WebServer", "192.168.1.101")
server2 = Server("DatabaseServer", "192.168.1.102", "online")
server3 = Server("FileServer", "192.168.1.103")
server4 = Server("test", "192.168.1.1.4")


# Display 
print(server1)
print(server2)
print(server3)

# Interact 
server1.start()
server2.stop()
server3.restart()
server4.stat()

print(f"Total number of servers: {Server.count}")
