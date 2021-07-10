import socket
import threading
from rich import print
from typing import TypedDict
from rich.console import Console
import time


HEADER: int = 64
PORT: int = 5050
SERVER: socket.gethostbyname = socket.gethostbyname(socket.gethostname())
ADDR: set = (SERVER, PORT)
FORMAT: str = 'utf-8'
DISCONNECT_MESSAGE: str = '!DISCONNECT'

server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


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


def handle_client(conn, addr) -> None:
    connected: bool = True
    while connected:
        name_length: int = conn.recv(HEADER).decode(FORMAT)
        if name_length:
            name_length = int(name_length)
            name: str = str(conn.recv(name_length).decode(FORMAT))
            print(f"{name} connected")
            conn.send(f"{name} joined".encode(FORMAT))
            time.sleep(5)
            connected = False
    conn.close()


def start() -> None:
    server.listen()
    console.print(f'{SERVER}')
    while True:
        conn, addr = server.accept()
        thread: threading.thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


console.print('Starting server')
start()
