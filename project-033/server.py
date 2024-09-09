import socket

HEADER = 64
HOST = '192.168.1.10' 
PORT = 5050   
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_cliente(conn, addr):
  print(f"[NEW CONNECTION] {addr} connected.")
  connected = True
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
      msg_length = int(msg_length)
      msg = conn.recv(msg_length).decode(FORMAT)
      if msg == DISCONNECT_MESSAGE:
        connected = False
      print(f'[{addr}] {msg}')
      conn.send("Message Receivd".encode(FORMAT))
  conn.close()

def start():
  print(f"[LISTENING] Server listning at {HOST}")
  server.listen()
  conn, addr = server.accept() # conn almacena el socket del cliente y addr la dirección IP y el puerto del cliente
  handle_cliente(conn, addr)

print("[STARTING] Server is starting...")
start()