import socket

#Server Side
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket sucessfully created!")

port = 9500 #1. accepts connections on port 9500
s.bind((socket.gethostbyname('localhost'),port)) #socket now is binded to port 9500

s.listen(5) #socket now listens to port 9500 for incoming messages
print('Socket is now Listening...')

def process_message(client_message):
    if client_message.decode("utf-8") == "Hello":
        return "Hi".encode("utf-8") #2. send "Hi" when the client sends "Hello"
    else:
        return "Goodbye".encode("utf-8") #3. sends "Goodbye" if clients send anything else

while True:
    client_socket,client_address = s.accept()
    print("Established connection with ", client_address)

    server_response = process_message( client_socket.recv(1024) )
    client_socket.send( server_response )
    client_socket.close()