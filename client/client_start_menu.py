import socket
from rich import print
from rich.text import Text
from rich.console import Console
from rich.panel import Panel
import os
import time
import threading

'''Clears terminal'''


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


main_title = Text.assemble(("""$$$$$$$$\\ $$\\                 
\\__$$  __|$$ |                
   $$ |   $$$$$$$\\   $$$$$$\\   
   $$ |   $$  __$$\\  \\____$$\\ 
   $$ |   $$ |  $$ | $$$$$$$ |
   $$ |   $$ |  $$ |$$  __$$ |
   $$ |   $$ |  $$ |\\$$$$$$$ |
   \\__|   \\__|  \\__| \\_______|\n""", "bold magenta"), ("""$$$$$$$\\                      
$$  __$$\\                     
$$ |  $$ | $$$$$$\  $$\   $$\\ 
$$$$$$$\ |$$  __$$\ \$$\ $$  |
$$  __$$\ $$ /  $$ | \$$$$  / 
$$ |  $$ |$$ |  $$ | $$  $$<  
$$$$$$$  |\$$$$$$  |$$  /\$$\\ 
\\_______/  \\______/ \\__/  \\__|""", "bold cyan"))


console: Console = Console()


'''
Sets variables used later on for socketing
'''
HEADER: int = 64
PORT: int = 5050
FORMAT: str = 'utf-8'
DISCONNECT_MESSAGE: str = '!DISCONNECT'


clear()


console.print(Panel.fit(main_title, border_style="red"))

'''
Prompts the user for the IP address
'''
SERVER: str = console.input('Server IP:')

ADDR: set = (SERVER, PORT)

'''Creates a connection to the server'''
client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

'''Function of which sends data to the server to connect the user'''


def join(name: str) -> None:
    name: bytes = name.encode(FORMAT)
    name_length: int = len(name)
    send_length: str = str(name_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(name)
    print(client.recv(1000).decode(FORMAT))


'''Function which will allow the user to send a message'''


def send_message(message: str) -> None:
    message: bytes = message.encode(FORMAT)
    msg_length: int = len(message)
    msg_length: str = str(msg_length).encode(FORMAT)
    msg_length += b' ' * (HEADER - len(msg_length))
    client.send(msg_length)
    client.send(message)
    time.sleep(0.1)


'''Prompts the user for their username'''
name: str = console.input('What is your name?:')
join(name)


def send_message_loop() -> None:
    while True:
        time.sleep(0.5)
        send_message(console.input('Type something: '))
        time.sleep(0.5)


def receive_messages_loop() -> None:
    while True:
        time.sleep(0.5)
        print(client.recv(1000).decode(FORMAT))
        time.sleep(0.5)


receive_messages_thread = threading.Thread(target=receive_messages_loop).start()
send_message_thread = threading.Thread(target=send_message_loop).start()