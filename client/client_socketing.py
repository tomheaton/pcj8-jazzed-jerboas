import socket
import select
import errno
from pynput import keyboard

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from utils import clear

import sys
from time import sleep

from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import input_dialog


console: Console = Console()


class MessageValidator(Validator):
    def validate(self, document):
        text = document.text

        if len(text) > 192:
            raise ValidationError(message='This input must be less than 192 characters long')


HEADER_LENGTH: int = 10

IP: str = input('Ip: ')
PORT: int = 8888
my_username: str = input("Username: ")

# Create a socket
client_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

client_socket.setblocking(False)

client_username: bytes = my_username.encode('utf-8')
username_header: bytes = f"{len(client_username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + client_username)

is_typing: bool = False


def send_message() -> None:
    # Wait for user to input a message
    global is_typing
    is_typing = True

    message: str = input_dialog(
        title='Type your message',
        # text=f'{client_username.decode("utf-8")} > ',
        validator=MessageValidator()
    ).run()

    if message:
        message: bytes = message.encode('utf-8')
        message_header: bytes = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
        print(f'{client_username.decode("utf-8")} > {message.decode("utf-8")}')
    is_typing = False


def receive_messages() -> None:
    global is_typing
    while True:
        while not is_typing:
            try:
                username_header = client_socket.recv(HEADER_LENGTH)

                if not len(username_header):
                    print('Connection closed by the server')
                    sys.exit()

                # Convert header to int value
                username_length: int = int(username_header.decode('utf-8').strip())

                # Receive and decode username
                username: str = client_socket.recv(username_length).decode('utf-8')

                # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
                message_header: bytes = client_socket.recv(HEADER_LENGTH)
                message_length: int = int(message_header.decode('utf-8').strip())
                message: str = str(client_socket.recv(message_length).decode('utf-8'))

                # Print message
                print(f'{username}: {message}')

            except IOError as e:
                # This is normal on non blocking connections - when there are no incoming data error is going to be raised
                # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
                # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
                # If we got different error code - something happened
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error: {}'.format(str(e)))
                    sys.exit()

                # We just did not receive anything
                continue

            except Exception as e:
                # Any other exception - something happened, exit
                print('Reading error: {}'.format(str(e)))
                sys.exit()
    # else:
    #     message: str = prompt(f'{username}: ', validator=MessageValidator())

    #     # If message is not empty - send it
    #     if message:

    #         # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
    #         message: bytes = message.encode('utf-8')
    #         message_header: bytes = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
    #         client_socket.send(message_header + message)
    #     else:
    #         continue

    #     is_typing = False


def hotkeys():
    with keyboard.GlobalHotKeys({
        '/': send_message,
            '<ctrl>+q': sys.exit, }) as h:
        h.join()


if __name__ == '__main__':
    hotkeys()
    receive_messages()
