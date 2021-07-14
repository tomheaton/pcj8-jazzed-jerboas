# The Server
import socketio
from aiohttp import web

sio = socketio.AsyncServer(async_mode="aiohttp")
app = web.Application()
sio.attach(app)


@sio.event
async def connect(sid, environ, auth):
    print(f"connect: {sid}")


@sio.event
async def disconnect(sid):
    print(f"disconnect: {sid}")


if __name__ == "__main__":
    web.run_app(app)
