import asyncio
import socket
import socketio
from rich.console import Console
from rich.prompt import Prompt, Confirm, IntPrompt
from components.client import Client
from components.common_utils import simple_callback

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


async def start_console():
    await asyncio.sleep(0.01)

    if Confirm.ask("returning user?"):
        # TODO: let user sign in to an account.
        username: str = Prompt.ask("enter username")
        password: str = Prompt.ask("enter password")
        await SIO.emit("login", {"username": username, "password": password}, callback=simple_callback)
    else:
        # TODO: let user create an account.
        CONSOLE.print("time to sign-up!")
        username: str = Prompt.ask("enter username")
        password: str = Prompt.ask("enter password")
        await SIO.emit("register", {"username": username, "password": password}, callback=simple_callback)

    await asyncio.sleep(0.01)

    if Confirm.ask("create a chatroom?"):
        # TODO: let user create a chatroom.
        chatroom_name: str = Prompt.ask("enter name for your chatroom")
        private: bool = Confirm.ask("private?")
        # TODO: check capacity input.
        capacity: int = IntPrompt.ask("enter room size")
        await SIO.emit("create_chatroom", {"room_name": chatroom_name, "private": private, "capacity": capacity})

    await asyncio.sleep(0.01)

    if Confirm.ask("join a chatroom?"):
        # TODO: let user join a chatroom.
        chatroom_name: str = Prompt.ask("enter chatroom to join")
        # TODO: check chatroom before joining. (do not let user create one by joining)
        await join_chatroom(chatroom_name)

    await asyncio.sleep(0.01)


async def console_loop():
    # TODO: let user input commands (etc. chat, join/leave, settings).
    while True:
        await asyncio.sleep(1)
        text: str = Prompt.ask("enter text")
        await SIO.emit("send_message", {"message": text, "room_name": CLIENT.get_chatroom().get_name()})


async def join_chatroom(name):
    await SIO.emit("join_chatroom", {"room_name": name})


async def leave_chatroom(name):
    await SIO.emit("leave_chatroom", {"room_name": name})


async def main():
    print("[CLIENT] Client started...")
    CLIENT.print_info()
    await SIO.connect(SERVER_IP)
    await asyncio.sleep(1)
    await start_console()
    await console_loop()
    await SIO.wait()


if __name__ == "__main__":
    asyncio.run(main())
