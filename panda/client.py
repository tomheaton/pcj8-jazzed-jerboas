import asyncio
import socket
import sys
sys.path.append('../')
import socketio
from rich.console import Console
from rich.prompt import Prompt, Confirm
from panda.components.client import Client
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


@SIO.event
async def send_message(sid, data):
    print(f"send message: {data}")


@SIO.event
async def receive_message(sid, data):
    print(f"receive message: {data}")
    CONSOLE.print(data)


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

    await join_chatroom(chatroom_id)


async def text_loop():
    while True:
        await asyncio.sleep(1)
        text: str = Prompt.ask("enter text")
        await SIO.emit("send_message", {"message": text})


async def join_chatroom(chatroom_id):
    await SIO.emit("join_chatroom", {"room_id": chatroom_id})


async def leave_chatroom(chatroom_id):
    await SIO.emit("leave_chatroom", {"room_id": chatroom_id})


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
