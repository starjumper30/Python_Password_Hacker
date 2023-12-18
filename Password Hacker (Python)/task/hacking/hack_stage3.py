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

    with socket.socket() as client_socket, open('passwords.txt', 'rt') as fh:
        client_socket.connect((args.host, args.port))
        for line in fh:
            candidate = line.rstrip()
            for flags in itertools.product([0, 1], repeat=len(candidate)):
                password = ''.join([t[0] if t[1] == 0 else t[0].upper() for t in zip(candidate, flags)])
                # print(password)
                client_socket.send(password.encode())
                response = client_socket.recv(1024).decode()
                if response == 'Connection success!':
                    print(password)
                    return


if __name__ == '__main__':
    main()
