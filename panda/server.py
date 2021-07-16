# The Server
import socket
import socketio
from aiohttp import web
from dotenv_config import Config
from components.server_utils import create_database, register_user, login_user, generate_uuid
from components.server import Server
from components.user import User
from components.chatroom import ChatRoom

# TODO: improve this?
config = Config(".env")
salt = config("SALT", str)

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
    globals().update(DATABASE=create_database("database_test.json"))
    DATABASE.dump()
    print("[SERVER] saving database")


def shutdown_server():
    print("[SERVER] server shutting down...")
    DATABASE.dump()
    print("[SERVER] saving database")
    # TODO: serialize and save chatrooms.
    for room in SERVER.chatrooms:
        room.purge()
    SERVER.purge()
    print("[SERVER] purging users")


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
async def create_chatroom(sid, data):
    print(f"create chatroom: {sid}, data: {data}")
    room = ChatRoom(data["room_name"], generate_uuid(), None, data["private"], data["capacity"])
    SERVER.chatrooms.append(room)
    await join_chatroom(sid, {"room_name": data["room_name"]})


@SIO.event
async def list_chatroom(sid, environ, auth):
    print(f"list chatroom: {sid}")
    for room in SERVER.get_chatrooms():
        print(room.get_name())


@SIO.event
async def join_chatroom(sid, data):
    print(f"{sid} joined chatroom, data: {data['room_name']}.")
    success: bool = False
    SIO.enter_room(sid, data["room_name"])


@SIO.event
async def leave_chatroom(sid, data):
    print(f"{sid} left chatroom {data['room_name']}.")
    success: bool = False
    SIO.leave_room(sid, data["room_name"])


@SIO.event
async def close_chatroom(sid, data):
    print(f"close chatroom: {sid}")
    print(f"{sid} closed chatroom {data['room_name']}.")
    success: bool = False
    await SIO.close_room(sid, data["room_name"])


@SIO.event
async def send_message(sid, data):
    print(f"send message: {sid}, data: {data}")
    await SIO.emit("receive_message", {"message": data["message"], "sender": sid}, room=data["room_name"])


@SIO.event
async def receive_message(sid, data):
    print(f"receive message: {sid}, data: {data}")


if __name__ == "__main__":
    setup_server()
    web.run_app(APP)
