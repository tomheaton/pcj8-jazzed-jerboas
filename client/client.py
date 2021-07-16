# Client
import asyncio
import socketio
from rich.console import Console
from rich.prompt import Prompt

sio = socketio.AsyncClient()
console = Console()
CONNECTED: bool = False
USERNAME = ""
ROOM = ""


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
    await sio.connect('http://localhost:8080')
    await asyncio.sleep(2)
    print("[CLIENT]: Running console...")
    await console_loop()


async def console_loop():
    if CONNECTED:
        name: str = Prompt.ask("enter username")
        globals().update(USERNAME=name)
        room_name: str = Prompt.ask("enter room name")
        globals().update(ROOM=room_name)
        await sio.emit("join_room", {"username": USERNAME, "room_name": ROOM})

    while True & CONNECTED:
        await asyncio.sleep(2)
        message: str = Prompt.ask("enter message")
        await asyncio.sleep(0.01)
        await sio.emit("send_message", {"username": USERNAME, "message": message, "room_name": ROOM})

if __name__ == "__main__":
    asyncio.run(main())
