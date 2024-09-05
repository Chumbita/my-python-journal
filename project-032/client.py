import socket

HOST = '192.168.1.10'    # IP Servidor
PORT = 5050    # Puerto de envío
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(ADDR)
server.sendall(b"Hola Mundo")

data = server.recv(1024)

print("[MESSAGE]", repr(data))