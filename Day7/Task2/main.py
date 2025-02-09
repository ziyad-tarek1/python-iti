import socket

def is_port_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  
    result = s.connect_ex((ip, port))  
    s.close()
    return result == 0  

ip_address = "192.168.120.128"  
port = 22  

if is_port_open(ip_address, port):
    print(f"Port {port} is open on {ip_address}")
else:
    print(f"Port {port} is closed on {ip_address}")
