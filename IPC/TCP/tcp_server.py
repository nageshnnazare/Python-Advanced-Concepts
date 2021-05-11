#TCP Server

import logging
import socket
import time

logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

#TCP Server
def server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)

    logging.info(f'Bind : {ip}:{port}')
    s.bind(address)

    logging.info(f'Listening...')
    s.listen(1)

    conn, addr = s.accept()
    logging.info(f'Connected to {conn}:{addr}')

    while True:
        data = conn.recv(1024)
        if not len(data) == 0:
            logging.info(f'Exiting')
            conn.close()
            break
        logging.info(f'Data received = {data}')

    logging.info(f'Closing the server')
    s.close()

def main():
    server('localhost', 2607)

if __name__ == '__main__':
    main()
    