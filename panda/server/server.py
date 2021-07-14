# The Server
import hashlib
import os
import socket
import uuid
import socketio
from aiohttp import web
from panda.components.server import Server
from panda.components.user import User
from server_utils import create_database, register_user, login_user
import dotenv

dotenv.load_dotenv()
salt = os.environ.get("SALT")
print(f"salt: {salt}")

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
    print("[SERVER] dumping db")


def shutdown_server():
    print("[SERVER] server shutting down...")
    DATABASE.dump()
    # TODO: save chatrooms.
    for room in SERVER.chatrooms:
        room.purge()
    SERVER.purge()


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
async def join_chatroom(sid, environ, auth):
    print(f"join chatroom: {sid}")
    success: bool = False


if __name__ == "__main__":
    setup_server()
    web.run_app(APP)
