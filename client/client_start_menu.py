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

            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            print(f'{username} > {message}')

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()

            continue

        except Exception as e:
            print('Reading error: '.format(str(e)))
            sys.exit()


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
