import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9500 #1. client connects to port 9500

s.connect((socket.gethostbyname('localhost'),port)) #IP address of this computer on the network

client_message = 'Hello'.encode("utf-8") #2. sends the message "Hello"
s.send(client_message)
server_response = ''
while True:
    response = s.recv(1024) #3. recieves a message from the server
    if len(response) <= 0:
        break
    server_response += response.decode("utf-8")

print(server_response)