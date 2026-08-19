import socket, sys

u = sys.argv[1] if len(sys.argv) > 2 else input("Username: ")
p = sys.argv[2] if len(sys.argv) > 2 else input("Password: ")

s = socket.socket()
s.connect(("127.0.0.1", 9000))
s.send(b"HELLO")
print(s.recv(1024).decode())    # USERNAME?
s.send(u.encode())
print(s.recv(1024).decode())    # PASSWORD?
s.send(p.encode())
print(s.recv(1024).decode())    # SUCCESS / FAIL
s.close()
