import socket, sys, hmac, hashlib

u = sys.argv[1] if len(sys.argv) > 2 else input("Username: ")
p = sys.argv[2] if len(sys.argv) > 2 else input("Password: ")

s = socket.socket()
s.connect(("127.0.0.1", 9001))
s.send(b"HELLO")
print(s.recv(1024).decode())                    # USERNAME?
s.send(u.encode())
chal = s.recv(1024).decode().split()[1]         # CHALLENGE <nonce>
print("CHALLENGE", chal)
resp = hmac.new(p.encode(), chal.encode(), hashlib.sha1).hexdigest()
print("RESPONSE", resp)
s.send(resp.encode())
print(s.recv(1024).decode())                    # SUCCESS / FAIL
s.close()
