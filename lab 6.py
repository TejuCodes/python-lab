import socket

host = "8.8.8.8"      # localhost
ports = [21, 22, 80, 443, 3306]   # few common ports

for port in ports:
    s = socket.socket()
    try:
        s.connect((host, port))
        print(f"Port {port} is OPEN")
    except:
        print(f"Port {port} is CLOSED")
    s.close()
