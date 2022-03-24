import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
MY_PORT = 65433  
CONN_PORT = 65432
DATA = b"pong"

with socket.socket(
    socket.AF_INET,  # use IPv4 protocol
    socket.SOCK_STREAM  # SOCK_STREAM -> tcp | SOCK_DGRAM -> udp
) as s:
    s.bind((HOST, MY_PORT))  # binding with the address
    for i in range(10):
        s.listen()
        conn, addr = s.accept()
        # return (conn, addr)
        # conn -> new socket object usable to send and receive data on the connection
        # addr -> address bound to the socket on the other end of the connection.
        with conn:
            data = conn.recv(1024)  # receive data from the socket (bufsize)
            print(data)
            if not data:
                break
            conn.send(DATA)
