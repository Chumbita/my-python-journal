import socket

HEADER = 64
HOST = '192.168.1.10' 
PORT = 5050   
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
  message = msg.encode(FORMAT)
  msg_length = len(message)
  send_length = str(msg_length).encode(FORMAT)
  send_length += b' ' * (HEADER - len(send_length))
  client.send(send_length)
  client.send(message)
  print(client.recv(1024).decode(FORMAT))

send("Hello Word!")
send("Hello Word!")
send("Hello Word!")
send(DISCONNECT_MESSAGE)