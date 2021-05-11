#TCP client

import logging
import socket
import time

logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

#TCP Client:
def download(server, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (server, port)
    logging.info(f'Connecting to our {server}:{port}')

    s.connect(address)
    logging.info(f'Connected')

    logging.info(f'Send')
    s.send(b'Hello \r\n')

    logging.info(f'Recv')
    data = s.recv(1024)

    logging.info(f'Closing')
    s.close()

    logging.info(f'Data : {data}')


def main():
    download('youtube.com', 80)

if __name__ == '__main__':
    main()
    