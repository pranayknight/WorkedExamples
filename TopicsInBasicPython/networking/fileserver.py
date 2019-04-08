import socket

host='localhost'
port=6767

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

print("Server listening to port:",port)
s.listen(1)

c, addr = s.accept()

fileName = c.recv(1024)
try:
    f = open(filename,'rb')
    content1 = f.read()
    c.send(content1)
    f.close()
except FileNotFoundError:
    c.send(b"File does not exists")

c.close()
