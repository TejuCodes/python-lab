import os

# Get your network range (example: 192.168.1.0/24)
network = "192.168.1."

print("Scanning your local network...\n")

for i in range(1, 255):
    ip = network + str(i)
    response = os.system(f"ping -n 1 -w 300 {ip} > nul")  # For Windows
    # For Linux/Mac use: os.system(f"ping -c 1 -W 1 {ip} > /dev/null")

    if response == 0:
        print(f"{ip} is ACTIVE")
    else:
        print(f"{ip} is inactive")


import os

network="192.168.1."
print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>")
for host in range(1,50):
    ip=network+str(host)
    result=os.system(f'ping -n 1 {ip} >nul')
    if result ==0:
        print(ip,"is open")
    else:
        print(ip,"is closed")
    host.close()
