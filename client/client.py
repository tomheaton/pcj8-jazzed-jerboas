# Client
import asyncio
import socketio
import rendering
import main as main_navigation
from rich.console import Console
from rich.prompt import Prompt, Confirm, IntPrompt


sio = socketio.AsyncClient()
console = Console()
CONNECTED: bool = False
USERNAME = ""
ROOM = ""
ROOMS: list = []


def set_rooms(data):
    globals().update(ROOMS=data["rooms"])


async def get_rooms():
    await sio.emit("get_rooms", callback=set_rooms)


@sio.event
async def connect():
    print('[CLIENT]: connected to server')
    globals().update(CONNECTED=True)


@sio.event
async def disconnect():
    print('[CLIENT]: disconnected from server')
    globals().update(CONNECTED=False)


@sio.event
async def send_message(sid, data):
    print(f'[CLIENT]: message sent {sid}, data: {data}')


@sio.event
async def receive_message(data):
    print(f"[{data['username']}]: {data['message']}")


async def main():
    print("[CLIENT]: Starting connection...")
    try:
        await sio.connect('http://localhost:8080')
    except ConnectionError as e:
        print("[CLIENT]: could not connect to server.")
    await asyncio.sleep(2)
    print("[CLIENT]: Running console...")
    await console_loop()


async def console_loop():
    # TODO: log the user in/make an account
    if CONNECTED:
        client_info = main_navigation.main_menu(logged_in=False, logged_in_as=None)
        globals().update(USERNAME=client_info[0].username)
        if Confirm.ask("returning user?"):
            # TODO: let user sign in to an account.
            username: str = Prompt.ask("enter username")
            password: str = Prompt.ask("enter password")
            # IF SUCCESS, create account and log them in
            globals().update(USERNAME=username)
            room_name: str = Prompt.ask("enter room name")
            globals().update(ROOM=room_name)
            await sio.emit("join_room", {"username": USERNAME, "room_name": ROOM})
        else:
            # TODO: let user create an account.
            console.print("time to sign-up!")
            username: str = Prompt.ask("enter username")
            password: str = Prompt.ask("enter password")
            # IF SUCCESS, create account and log them in
            globals().update(USERNAME=username)
            room_name: str = Prompt.ask("enter room name")
            globals().update(ROOM=room_name)
            await sio.emit("join_room", {"username": USERNAME, "room_name": ROOM})

        await asyncio.sleep(0.01)

        if Confirm.ask("join a chatroom?"):
            # TODO: let user join a chatroom.
            chatroom_name: str = Prompt.ask("enter chatroom to join")
            # TODO: check chatroom before joining. (do not let user create one by joining)
        if Confirm.ask("create a chatroom?"):
            # TODO: let user create a chatroom.
            chatroom_name: str = Prompt.ask("enter name for your chatroom")
            private: bool = Confirm.ask("private?")
            # TODO: check capacity input.
            capacity: int = IntPrompt.ask("enter room size")

        await asyncio.sleep(0.01)

    while True and CONNECTED:
        await asyncio.sleep(2)
        message: str = Prompt.ask("enter message")
        await asyncio.sleep(0.01)
        await sio.emit("send_message", {"username": USERNAME, "message": message, "room_name": ROOM})

if __name__ == "__main__":
    asyncio.run(main())
