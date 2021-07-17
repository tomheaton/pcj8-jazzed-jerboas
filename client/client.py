# Client
import asyncio
import socketio
import rendering
import main as main_navigation
from rich.console import Console
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.live import Live
from utils import clear, User

sio = socketio.AsyncClient()
console = Console()
CONNECTED: bool = False
USERNAME = ""
ROOM = ""
ROOMS: list = []

messages_to_show: list = []


async def exit_client():
    # print("[CLIENT]: exiting client application.")
    await sio.disconnect()
    exit()


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
    global messages_to_show
    messages_to_show.append([data["username"], data["message"]])


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
    global messages_to_show
    # TODO: log the user in/make an account
    if CONNECTED:
        client_info = main_navigation.main_menu(logged_in=False, logged_in_as=None)
        if client_info[0] == "create":
            join_or_create, user, session_id, password, room_size_max, server_type = client_info
            if server_type == "private":
                private = True
            else:
                private = False
        if join_or_create == "create":
            await sio.emit("create_room", {"room_name": session_id, "private": private, "password": password, "capacity": room_size_max, "room_owner": user.username})
        if join_or_create == "join":
            await sio.emit("join_room")

        clear()
        await asyncio.sleep(0.01)

    while True and CONNECTED:
        await asyncio.sleep(2)
        clear()
        global messages_to_show
        if len(messages_to_show) != 0:
            index_of_i = -1
            for i in messages_to_show:
                index_of_i += 1
                with Live("", refresh_per_second=14) as live:
                    render_user = User(i[0], "NotImportant", preferences=user.preferences)
                    rendering.render_message(i[1], render_user, live=live)
                    messages_to_show.pop(index_of_i)
            clear()
        message = rendering.prompt(user)
        await asyncio.sleep(0.01)
        await sio.emit("send_message", {"username": user.username, "message": message, "room_name": session_id})

if __name__ == "__main__":
    asyncio.run(main())
