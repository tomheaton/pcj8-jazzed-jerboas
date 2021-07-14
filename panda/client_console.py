import threading
import time
import socketio
from classes import Client
import socket
from rich.text import Text
from rich.prompt import Prompt
from rich.panel import Panel
from rich.screen import Screen
from rich.console import Console, RenderGroup
from rich.align import Align

CLIENT_NAME = socket.gethostname()
CLIENT_ADDRESS = socket.gethostbyname(CLIENT_NAME)
CLIENT = Client(CLIENT_ADDRESS, CLIENT_NAME)
SERVER_IP = "http://localhost:8080"
SIO = socketio.AsyncClient()
CONSOLE = Console()


def login():
    pass


def start_console():
    name: str = CONSOLE.input("enter name: ")
    password: str = CONSOLE.input("enter password: ")


async def connect_to_server():
    await SIO.connect(SERVER_IP)
    await SIO.wait()


def main():
    print("client started")
    CLIENT.print_info()


if __name__ == "__main__":
    main()
