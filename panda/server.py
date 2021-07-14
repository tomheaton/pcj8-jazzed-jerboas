# The Server
import os
import socket
import dotenv
import socketio
from aiohttp import web
from server.server_utils import create_database, register_user, login_user
from components.server import Server
from components.user import User

dotenv.load_dotenv()
salt = os.environ.get("SALT")

# TODO: move some of this to the Server class.
SERVER_NAME = socket.gethostname()
SERVER_ADDRESS = socket.gethostbyname(SERVER_NAME)
APP = web.Application()
SIO = socketio.AsyncServer(async_mode="aiohttp")
SIO.attach(APP)
# TODO: maybe load saved chatrooms?
SERVER = Server(SERVER_ADDRESS, SERVER_NAME)

global DATABASE


def setup_server():
    SERVER.print_info()
    print("[SERVER] server starting up...")
    globals().update(DATABASE=create_database("server/database_test.json"))
    DATABASE.dump()
    print("[SERVER] saving database")


def shutdown_server():
    print("[SERVER] server shutting down...")
    DATABASE.dump()
    print("[SERVER] saving database")
    # TODO: save chatrooms.
    for room in SERVER.chatrooms:
        room.purge()
    SERVER.purge()
    print("[SERVER] users purging users")


@SIO.event
async def connect(sid, environ, auth):
    print(f"connect: {sid}")


@SIO.event
async def disconnect(sid):
    print(f"disconnect: {sid}")


@SIO.event
async def login(sid, data):
    print(f"login: {sid}, data: {data}")
    success = login_user(data.get("username"), data.get("password"), salt, DATABASE)

    if success:
        user_object = DATABASE.search_username(data.get("username"))
        user: User = User(**user_object)
        SERVER.add_user(user)
        print(f"users count: {len(SERVER.users)}")
        return "success", "you logged in!"
    else:
        return "failure", "you were not logged in!"


@SIO.event
async def logout(sid):
    print(f"logout: {sid}")


@SIO.event
async def register(sid, data):
    print(f"register: {sid}, data: {data}")
    # register_user(data.get("username"), data.get("password"), salt)
    register_user(data.get("username"), data.get("password"), salt, DATABASE)
    return "ok", "okay"


@SIO.event
async def create_chatroom(sid, environ, auth):
    print(f"create chatroom: {sid}")


@SIO.event
async def join_chatroom(sid, data):
    print(f"{sid} joined chatroom {data['room_id']}.")
    success: bool = False
    SIO.enter_room(sid, data["room_id"])


@SIO.event
async def leave_chatroom(sid, data):
    print(f"{sid} left chatroom {data['room_id']}.")
    success: bool = False
    SIO.leave_room(sid, data["room_id"])


@SIO.event
async def close_chatroom(sid, data):
    print(f"close chatroom: {sid}")
    print(f"{sid} closed chatroom {data['room_id']}.")
    success: bool = False
    await SIO.close_room(sid, data["room"])


@SIO.event
async def send_message(sid, data):
    print(f"send message: {data}")
    await SIO.emit("receive_message", {"message": data["message"], "sender": sid}, room=data["room_id"])


@SIO.event
async def receive_message(sid, data):
    print(f"receive message: {data}")


if __name__ == "__main__":
    setup_server()
    web.run_app(APP)
