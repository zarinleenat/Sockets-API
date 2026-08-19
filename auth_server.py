import socket

USER, PASS = "alice", "hunter2"

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 9000))
s.listen(1)
print("Plaintext auth server on 127.0.0.1:9000")

while True:
    c, addr = s.accept()
    c.recv(1024)                                  # 1. HELLO
    c.send(b"USERNAME?")                          # 2. ask username
    u = c.recv(1024).decode().strip()             # 3. username
    c.send(b"PASSWORD?")                          # 4. ask password
    p = c.recv(1024).decode().strip()             # 5. password
    ok = (u == USER and p == PASS)
    c.send(b"SUCCESS" if ok else b"FAIL")         # 6. result
    print(addr, u, p, "->", "SUCCESS" if ok else "FAIL")
    c.close()
