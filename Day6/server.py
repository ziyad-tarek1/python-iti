
class Server:
    count = 0  
#############################################################################################################
    def __init__(self, name, ip_address, status="offline"):
        self.name = name
        self.ip_address = ip_address
        self.status = status
        Server.count += 1
        self.server_id = Server.count  # Unique ID for each server

#############################################################################################################

    def start(self):
        if self.status == "offline":
            self.status = "online"
            print(f"{self.name} is now online.")
        else:
            print(f"{self.name} is already online.")

#############################################################################################################

    def stop(self):
        if self.status == "online":
            self.status = "offline"
            print(f"{self.name} is now offline.")
        else:
            print(f"{self.name} is already offline.")

#############################################################################################################

    def restart(self):
        if self.status == "online":
            self.stop()
            self.start()
            print(f"{self.name} has been restarted.")
        else:
            print(f"Server {self.server_id} ({self.name}) is offline and will be powered on.")
            self.start()
#############################################################################################################

    def stat(self):
        print(f"Server ID: {self.server_id}, Name: {self.name}, Status: {self.status}.")

#############################################################################################################
    def __str__(self):
        return f"Server ID: {self.server_id}, Name: {self.name}, IP Address: {self.ip_address}, Status: {self.status}"
