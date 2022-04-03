import socket

HOST = socket.gethostname()
MY_PORT = 65432
CONN_PORT = 65433
DATA = b"ping"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, MY_PORT))
    s.connect((HOST, CONN_PORT))
    s.send(DATA)
    data = s.recv(1024)

    #s.listen()
    #conn, addr = s.accept()

    data = s.recv(1024)
    print(data)
    s.send(DATA)
