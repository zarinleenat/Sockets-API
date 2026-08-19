import socket, hmac, hashlib, os

USER, PASS = "alice", b"hunter2"

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 9001))
s.listen(1)
print("Challenge-handshake server on 127.0.0.1:9001")

while True:
    c, addr = s.accept()
    c.recv(1024)                                          # 1. HELLO
    c.send(b"USERNAME?")                                  # 2. ask username
    u = c.recv(1024).decode().strip()                     # 3. username
    nonce = os.urandom(8).hex().encode()                  # random challenge
    c.send(b"CHALLENGE " + nonce)                         # 4. send challenge
    resp = c.recv(1024).strip()                           # 5. HMAC response
    expected = hmac.new(PASS, nonce, hashlib.sha1).hexdigest().encode()
    ok = (u == USER) and hmac.compare_digest(resp, expected)
    c.send(b"SUCCESS" if ok else b"FAIL")                 # 6. result
    print(addr, u, nonce.decode(), "->", "SUCCESS" if ok else "FAIL")
    c.close()
