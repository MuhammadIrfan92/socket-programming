import socket
import threading


# first message to the server from the client will be the length of the message that the
# client will send to the server
HEADER = 64
# Port number for socket
PORT = 5050

# IP address for the socket (INET of this device)
SERVER = socket.gethostbyname(socket.gethostname())
# Socket binding address
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# Creating a socket
# AF_INET for IPv4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding the socket to the specified address
server.bind(ADDR)


def handle_client(conn, addr):
    # this function will run for each client
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        # receive data from client
        # converting msg from bytes format to a string
        msg_length = conn.recv(HEADER).decode(FORMAT)  # receive number of bytes to receive from the client
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] Says: {msg}")
            conn.send("Message received".encode(FORMAT))

    conn.close()


def start():
    # start listening for new connections
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    # Continue to listen for infinite time
    while True:
        # wait for the connection to occur
        # 'addr' has the ip address and port from which the connection request came from
        # 'conn' is the socket object that allows the communication back to the client
        conn, addr = server.accept()
        # start new thread to handle the new connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        # start the thread
        thread.start()
        # Printing number of active threads (Client connections) subtracting 1 because
        # 1 thread is always running to listen for the new connections
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


print("[Starting] server is starting...")
start()
