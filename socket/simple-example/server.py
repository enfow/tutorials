import socket

HOST = socket.gethostname()

SERVER_PORT = 65432
DATA = b"pong"

with socket.socket(
    socket.AF_INET,  # use IPv4 protocol
    socket.SOCK_STREAM  # SOCK_STREAM -> tcp | SOCK_DGRAM -> udp
) as s:
    s.bind((HOST, SERVER_PORT))  # binding with the address

    s.listen(1)  # set listen condition (e.g. the number of available conn.)
    # socket.accept() returns (conn, addr)
    # conn -> new socket object usable to send and receive data on the connection
    # addr -> address bound to the socket on the other end of the connection.
    conn, addr = s.accept()  # accept new connection [SERVER ONLY]
    for i in range(10):
        with conn:
            data = conn.recv(1024)  # receive data from the socket (bufsize)
            print(data)
            if not data:
                break
            conn.send(DATA)

# error 1
# OSError: [Errno 9] Bad file descriptor
# with `data = conn.recv(1024)`
