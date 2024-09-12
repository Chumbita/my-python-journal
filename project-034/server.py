import socket
import threading

HEADER = 64
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def handle_client(conn, addr):
  print(f"[NEW CONNECTION] {addr} conected.")
  connected = True
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
      msg_length = int(msg_length)
      msg = conn.recv(msg_length).decode(FORMAT)
      if msg == DISCONNECT_MESSAGE:
        connected = False
      print(f"[CLIENT] {addr}: {msg}")
      conn.send("Message received".encode(FORMAT))
  conn.close()

def start():
  print(f"[LISTENING] Server listning at {HOST}")
  server.listen()
  while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
  server.bind(ADDR)
  print("[STARTING] Server is starting...")
  start()