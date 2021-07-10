import time
import socket
import threading
from rich import print
from typing import TypedDict
from rich.console import Console

# Variables used later on
HEADER: int = 64
PORT: int = 5050

# Creates a server address
SERVER: socket.gethostbyname = socket.gethostbyname(socket.gethostname())
ADDR: set = (SERVER, PORT)
FORMAT: str = "utf-8"
DISCONNECT_MESSAGE: str = "!DISCONNECT"

server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

clients = []


class BoxStyle(TypedDict):
    """
    Storing user preferences for the box.
    """
    username_color: str
    outline_color: str
    text_color: str


class User(TypedDict):
    """
    Storing username and user-preferences.
    """
    username: str
    uuid: str
    style: BoxStyle


console: Console = Console()

messages = []


def handle_client(conn, addr) -> None:
    connected: bool = True

    # Receives name from the client
    name_length: int = conn.recv(HEADER).decode(FORMAT)
    if name_length:
        name_length = int(name_length)
        name: str = str(conn.recv(name_length).decode(FORMAT))
        print(f"{name} connected")
        clients.append(conn)
        for client in clients:
            client.send(f"{name} joined".encode(FORMAT))

    while connected:

        # Receives messages from the client
        msg_length: int = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            message: str = str(conn.recv(msg_length).decode(FORMAT))
            print(f"{name}: {message}")
            messages.append([name, message])
            print(messages)
            for client in clients:
                client.send(f"{messages[-1][0]}: {messages[-1][1]}".encode(FORMAT))

    conn.close()


def start() -> None:
    server.listen()
    console.print(f'{SERVER}')
    while True:
        # Accepts connection to the server
        conn, addr = server.accept()
        # Creates a thread to handle each individual connection
        thread: threading.thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


console.print("Starting server")
start()
