<<<<<<< HEAD
# NOTE: NOT MY CODE

import socket
import select
import errno
from multiprocessing import Process
import time
import threading

HEADER_LENGTH = 10

IP = input('Type in the IP address: ')
PORT = 1234
my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))

client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)


def func_1():
    while True:
        time.sleep(0.1)
        try:
            message = input(f'{my_username} > ')

            if message:

                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                client_socket.send(message_header + message)
        except EOFError:
            continue


def func_2():
    while True:
        time.sleep(0.1)
        try:

            username_header = client_socket.recv(HEADER_LENGTH)

            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()
=======
import os
import socket
import threading
import time

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


def clear() -> int:
    """
    Clears terminal
    """
    return os.system('cls' if os.name == 'nt' else 'clear')


main_title = Text.assemble(
    ("""$$$$$$$$\\ $$\\
\\__$$  __|$$ |
   $$ |   $$$$$$$\\   $$$$$$\\
   $$ |   $$  __$$\\  \\____$$\\
   $$ |   $$ |  $$ | $$$$$$$ |
   $$ |   $$ |  $$ |$$  __$$ |
   $$ |   $$ |  $$ |\\$$$$$$$ |
   \\__|   \\__|  \\__| \\_______|\n""",
     "bold magenta"),
    ("""$$$$$$$\\
$$  __$$\\
$$ |  $$ | $$$$$$\  $$\   $$\\
$$$$$$$\ |$$  __$$\ \$$\ $$  |
$$  __$$\ $$ /  $$ | \$$$$  /
$$ |  $$ |$$ |  $$ | $$  $$<
$$$$$$$  |\$$$$$$  |$$  /\$$\\
\\_______/  \\______/ \\__/  \\__|""",
     "bold cyan")
)

console: Console = Console()

# Sets variables used later on for use with sockets
HEADER: int = 64
PORT: int = 5050
FORMAT: str = 'utf-8'
DISCONNECT_MESSAGE: str = '!DISCONNECT'

clear()

console.print(Panel.fit(main_title, border_style="red"))

# Prompts the user for the IP address
SERVER: str = console.input("Server IP:")

ADDR: set = (SERVER, PORT)

# Creates a connection to the server
client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def join(name: str) -> None:
    """
    Function of which sends data to the server to connect the user
    """
    name: bytes = name.encode(FORMAT)
    name_length: int = len(name)
    send_length: str = str(name_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(name)
    print(client.recv(1000).decode(FORMAT))


def send_message(message: str) -> None:
    """
    Function which will allow the user to send a message
    """
    message: bytes = message.encode(FORMAT)
    msg_length: int = len(message)
    msg_length: str = str(msg_length).encode(FORMAT)
    msg_length += b' ' * (HEADER - len(msg_length))
    client.send(msg_length)
    client.send(message)
    time.sleep(0.1)
>>>>>>> 78d6652c53a630635fdd23c29241ea781c7f6ebf

            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

<<<<<<< HEAD
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
=======
# Prompts the user for their username
name: str = console.input("What is your name?: ")
join(name)
>>>>>>> 78d6652c53a630635fdd23c29241ea781c7f6ebf

            print(f'{username} > {message}')

<<<<<<< HEAD
        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()
=======
def send_message_loop() -> None:
    """
    Send message loop function.
    """
    while True:
        send_message(console.input("Type something: "))
>>>>>>> 78d6652c53a630635fdd23c29241ea781c7f6ebf

            continue

<<<<<<< HEAD
        except Exception as e:
            print('Reading error: '.format(str(e)))
            sys.exit()
=======
def receive_messages_loop() -> None:
    """
    Receive message loop function.
    """
    while True:
        print(client.recv(1000).decode(FORMAT))
>>>>>>> 78d6652c53a630635fdd23c29241ea781c7f6ebf


if __name__ == '__main__':
    # process_1: Process = Process(target=func_1)
    # process_1.start()
    # process_1.join()
    # process_2: Process = Process(target=func_2)
    # process_2.start()
    # process_2.join()
    thread_1: threading.Thread = threading.Thread(target=func_1)
    thread_1.start()
    thread_2: threading.Thread = threading.Thread(target=func_2)
    thread_2.start()
