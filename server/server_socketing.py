import socket
import select
import sys
from typing import Union

HEADER_LENGTH = 10

IP: str = socket.gethostbyname(socket.gethostname())
PORT: int = 8888

# Create a socket
server_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

# List of sockets for select.select()
sockets_list: list = [server_socket]

# List of connected clients - socket as a key, user header and name as data
clients: dict = {}

print(f'Listening for connections on {IP}:{PORT}...')


def receive_message(client_socket) -> Union[dict, bool]:
    try:
        message_header: bytes = client_socket.recv(HEADER_LENGTH)

        # If we received no data, client gracefully closed a connection, for example using socket.close() or
        # socket.shutdown(socket.SHUT_RDWR)
        if not len(message_header):
            return False

        message_length: int = int(message_header.decode('utf-8').strip())

        # Return an object of message header and message data
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except Exception:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:

            client_socket, client_address = server_socket.accept()

            # Client should send his name right away, receive it
            user: Union[dict, bool] = receive_message(client_socket)

            # If False - client disconnected before he sent his name
            if user is False:
                continue

            # Add accepted socket to select.select() list
            sockets_list.append(client_socket)

            # Also save username and username header
            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(
                *client_address, user['data'].decode('utf-8')))

            for client in clients:
                client.send('{} joined'.format(
                    user['data'].decode('utf-8')).encode('utf-8'))

        # Else existing socket is sending a message
        else:

            # Receive message
            message: Union[dict, bool] = receive_message(notified_socket)

            # If False, client disconnected, cleanup
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                for client in clients:
                    client.send('{} left'.format(
                        clients[notified_socket]['data'].decode('utf-8')).encode('utf-8'))

                # Remove from list for socket.socket()
                sockets_list.remove(notified_socket)

                # Remove from our list of users
                del clients[notified_socket]

                continue

            # Get user by notified socket, so we will know who sent the message
            user: Union[dict, bool] = clients[notified_socket]

            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            # Iterate over connected clients and broadcast message
            for client_socket in clients:
                client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:

        # Remove from list for socket.socket()
        sockets_list.remove(notified_socket)

        # Remove from our list of users
        del clients[notified_socket]
