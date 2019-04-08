import socket

host='localhost'
port=4000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

print("Server listening to port:",port)
s.listen(1)

c, addr = s.accept()

print("Connection from:",str(addr))

c.send(b"Hello, how are you ") # this is also a way to convert to binary
c.send("Bye".encode())       #sending should be in this form only i.e. binary
c.close()
