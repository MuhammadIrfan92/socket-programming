import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT) # encodes the message(string) to byte like object
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length)) # byte representation of space
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))


send("Hello World")
send("Hello lol")
send("Hello bol")
send("Hello tol")
send(DISCONNECT_MESSAGE)