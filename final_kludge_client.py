import socket
from Crypto.Cipher import AES
key=b"Thekludgekey0001"
nonce=b"Thekludgenonce1"

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect((socket.gethostbyname(socket.gethostname()),12345))


cipher=AES.new(key, AES.MODE_EAX,nonce)

file_name = client_socket.recv(10).decode(encoding="utf-8")
print(file_name ,end="\n")
file_size=client_socket.recv(2).decode(encoding="utf-8")
print(file_size)

file=open(file_name ,"wb")

done=False

file_bytes=b""

while not done:
    data=client_socket.recv(1024)
    if file_bytes[-5:]==b"<END>":
        done=True
    else:
        file_bytes +=data

file.write(cipher.decrypt(file_bytes[:-5]))

file.close()


#with open(file_name ,'rb') as fi:
#content = fi.read()
#print(content)


client_socket.close()





