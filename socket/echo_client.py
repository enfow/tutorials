import socket

HOST = "0.0.0.0"  # The server's hostname or IP address
MY_PORT = 65432
CONN_PORT = 65433
DATA = b"ping"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, MY_PORT))
    s.connect((HOST, CONN_PORT))
    s.send(DATA)
    data = s.recv(1024)

    for i in range(10):
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.send(DATA)

print(f"Received {data!r}")
