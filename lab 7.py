import socket

# Create socket
server = socket.socket()

# Bind to local machine and port
server.bind(("localhost", 5000))

# Listen for connection
server.listen(1)
print("Server is waiting for connection...")

conn, addr = server.accept()
print("Connected with:", addr)

# Receive data
data = conn.recv(1024).decode()
print("Received from client:", data)

conn.close()



import socket

# Create client socket
client = socket.socket()

# Connect to server
client.connect(("localhost", 5000))

# Send data (traffic)
message = "Hello Server, this is client traffic!"
client.send(message.encode())

print("Data sent to server.")

client.close()
