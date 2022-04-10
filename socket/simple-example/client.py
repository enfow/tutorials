import socket

HOST = socket.gethostname()

CLIENT_PORT = 65433
SERVER_PORT = 65432
DATA = b"ping"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, CLIENT_PORT))
    s.connect((HOST, SERVER_PORT))  # request new connection [CLIENT ONLY]

    for i in range(10):
        s.send(DATA)
        data = s.recv(1024)
        print(data)
        if not data:
            break
