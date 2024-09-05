import socket

# HOST = socket.gethostbyname(socket.gethostname())
HOST = '192.168.1.10'    # IP Servidor 
PORT = 5050   # Puerto de escucha
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_cliente(conn, addr):
  print(f"[NEW CONNECTION] {addr} connected.")
  connected = True
  while connected:
    data = conn.recv(1024)
    conn.sendall(data)

def start():
  server.listen()
  conn, addr = server.accept() # conn almacena el socket del cliente y addr la dirección IP y el puerto del cliente
  handle_cliente(conn, addr)

print("[STARTING] Server is starting...")
start()