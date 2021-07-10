import socket
from rich import print
from rich.text import Text
from rich.console import Console
from rich.panel import Panel
import os
import time

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

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








HEADER: int = 64
PORT: int = 5050
FORMAT: str = 'utf-8'
DISCONNECT_MESSAGE: str = '!DISCONNECT'

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
console.print(Panel.fit(main_title, border_style="red"))
SERVER: str = console.input('Server IP:')

ADDR: set = (SERVER, PORT)


client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def join(name: str) -> None:
    name: bytes = name.encode(FORMAT)
    name_length: int = len(name)
    send_length: str = str(name_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(name)
    print(client.recv(1000).decode(FORMAT))


name: str = console.input('What is your name?:')
join(name)

time.sleep(10)
clear()
