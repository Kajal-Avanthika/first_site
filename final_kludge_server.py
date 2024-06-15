import socket
import os
from Crypto.Cipher import AES 
key=b"Thekludgekey0001"
nonce=b"Thekludgenonce1"


#first building a server socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((socket.gethostbyname(socket.gethostname()),12345)) #choosing arbitrary port address and passing a tuple to bind function
server_socket.listen() #Listening for a client connection

cipher=AES.new(key,AES.MODE_EAX) 
nonce=cipher.nonce

file_size=  os.path.getsize(r"C:\Users\kajal\Desktop\file11.txt")
with open(r"C:\Users\kajal\Desktop\file11.txt","rb") as f:
    data=f.read()

encrypted_file =cipher.encrypt(data)

while True:
    client_socket,client_address=server_socket.accept()
    print(f"Connected to client address {client_address} ")
    client_socket.send("file11.txt".encode(encoding="utf-8"))
    client_socket.send(str(file_size).encode(encoding="utf-8"))
    client_socket.sendall(encrypted_file)
    client_socket.send(b"<END>")

    server_socket.close()
    break

#success









