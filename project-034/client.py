import socket

HEADER = 64
HOST = "192.168.1.10"
PORT = 5050
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def send(msg):
  message = msg.encode(FORMAT)
  msg_length = len(message)
  send_length = str(msg_length).encode(FORMAT)
  send_length += b' ' * (HEADER - len(send_length))
  client.send(send_length)
  client.send(message)
  print(f"[SERVER] {HOST} : {client.recv(64).decode(FORMAT)}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
  client.connect(ADDR)
  connected = True
  while connected:
    msg = input('Send a message to the server: ')
    if msg == DISCONNECT_MESSAGE:
      connected = False
    send(msg)
