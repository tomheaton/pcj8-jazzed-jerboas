import asyncio
import socketio
from panda.components.client import Client
import socket
from rich.prompt import Prompt, Confirm
from rich.console import Console

# TODO: move some of this to the Client class.
CLIENT_NAME = socket.gethostname()
CLIENT_ADDRESS = socket.gethostbyname(CLIENT_NAME)
CLIENT = Client(CLIENT_ADDRESS, CLIENT_NAME)
SERVER_IP = "http://localhost:8080"
SIO = socketio.AsyncClient()
CONSOLE = Console()


@SIO.event
async def connect():
    print("[CLIENT] Connected to server.")
    # await SIO.emit("join_chat", {"room": room_name, "name": client_name})


@SIO.event
async def disconnect():
    print("[CLIENT] Disconnected from server.")
    # await SIO.emit("join_chat", {"room": room_name, "name": client_name})


def callback_message(a, b):
    print(f"callback: {a}, {b}")


async def start_console():
    await asyncio.sleep(0.01)
    if Confirm.ask("returning user?"):
        username: str = Prompt.ask("enter username")
        password: str = Prompt.ask("enter password")
        await SIO.emit("login", {"username": username, "password": password}, callback=callback_message)
    else:
        CONSOLE.print("time to sign-up!")
        username: str = Prompt.ask("enter username")
        password: str = Prompt.ask("enter password")
        await SIO.emit("register", {"username": username, "password": password}, callback=callback_message)

    chatroom_id: str = Prompt.ask("enter chatroom to join")


async def text_loop():
    while True:
        await asyncio.sleep(1)
        query: str = Prompt.ask("enter query")


async def main():
    print("[CLIENT] Client started...")
    CLIENT.print_info()
    await SIO.connect(SERVER_IP)
    await asyncio.sleep(1)
    await start_console()
    await text_loop()
    await SIO.wait()


if __name__ == "__main__":
    asyncio.run(main())
