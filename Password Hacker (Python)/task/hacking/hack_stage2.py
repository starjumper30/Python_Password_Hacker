# write your code here
import argparse
import socket
import itertools
import string

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


def main():
    """"""
    args = parse_args()
    with socket.socket() as client_socket:
        client_socket.connect((args.host, args.port))
        chars = string.ascii_lowercase + string.digits
        for i in range(1, 3):
            for tuples in itertools.product(chars, repeat=i):
                password = ''.join(tuples)
                client_socket.send(password.encode())
                response = client_socket.recv(1024).decode()
                if response == 'Connection success!':
                    print(password)
                    break


if __name__ == '__main__':
    main()
