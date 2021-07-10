# NOTE: NOT MY CODE

import socket
import select
import errno
from multiprocessing import Process
import time
import threading
from rich.text import Text
from rich.console import Console
import os
import sys


def clear() -> NoneType:
    """
    Clears terminal
    """
    return os.system('cls' if os.name == 'nt' else 'clear')


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


HEADER_LENGTH: int = 10

clear()

IP: str = input('Type in the IP address: ')
PORT: int = 8000
my_username: str = input("Username: ")

client_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))

client_socket.setblocking(False)

username: bytes = my_username.encode('utf-8')
username_header: str = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)


# def func_1():
#     while True:
#         time.sleep(0.1)
#         try:
#             message = input(f'{my_username} > ')

#             if message:

#                 message = message.encode('utf-8')
#                 message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
#                 client_socket.send(message_header + message)
#         except EOFError:
#             continue


# def func_2():
#     while True:
#         time.sleep(0.1)
#         try:

#             username_header = client_socket.recv(HEADER_LENGTH)

#             if not len(username_header):
#                 print('Connection closed by the server')
#                 sys.exit()

#             username_length = int(username_header.decode('utf-8').strip())
#             username = client_socket.recv(username_length).decode('utf-8')

#             message_header = client_socket.recv(HEADER_LENGTH)
#             message_length = int(message_header.decode('utf-8').strip())
#             message = client_socket.recv(message_length).decode('utf-8')

#             print(f'{username} > {message}')

#         except IOError as e:
#             if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
#                 print('Reading error: {}'.format(str(e)))
#                 sys.exit()

#             continue

#         except Exception as e:
#             print('Reading error: '.format(str(e)))
#             sys.exit()


# if __name__ == '__main__':
#     # process_1: Process = Process(target=func_1)
#     # process_1.start()
#     # process_1.join()
#     # process_2: Process = Process(target=func_2)
#     # process_2.start()
#     # process_2.join()
#     thread_1: threading.Thread = threading.Thread(target=func_1)
#     thread_1.start()
#     thread_2: threading.Thread = threading.Thread(target=func_2)
#     thread_2.start()
if __name__ == '__main__':
    while True:

        # Wait for user to input a message
        message: str = input(f'{my_username} > ')

        # If message is not empty - send it
        if message:

            # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
            message: bytes = message.encode('utf-8')
            message_header: str = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)

        try:
            # Now we want to loop over received messages (there might be more than one) and print them
            while True:

                # Receive our "header" containing username length, it's size is defined and constant
                username_header: bytes = client_socket.recv(HEADER_LENGTH)

                # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
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
                message: str = client_socket.recv(message_length).decode('utf-8')

                # Print message
                print(f'{username} > {message}')

        except IOError as e:
            # This is normal on non blocking connections - when there are no incoming data error is going to be raised
            # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
            # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
            # If we got different error code - something happened
            if e.errno is not errno.EAGAIN and e.errno is not errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()

            # We just did not receive anything
            continue

        except Exception as e:
            # Any other exception - something happened, exit
            print('Reading error: '.format(str(e)))
            sys.exit()
