#Blocking and non-blocking Sockets
#Blocking stops
#Non-blocking runs in the background

import logging
import socket
import select

logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

#Blocking Socket
def create_blocking(host, ip):
    logging.info(f'Blocking - creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info('Blocking - connecting...')
    s.connect((host,ip))

    logging.info(f'Blocking - connected...')
    logging.info(f'Blocking - sending...')
    s.send(b'hello\r\n')

    logging.info(f'Blocking - waiting...')
    data = s.recv(1024)
    logging.info(f'Blocking - Data = {len(data)}')

    logging.info(f'Blocking - closing...')
    s.close()

#Non-Blocking Socket
def create_nonblocking(host, port):
    logging.info(f'Non-blocking - creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info(f'Non-blocking - connecting...')
    ret = s.connect_ex((host, port)) # Blocking

    if ret != 0:
        logging.info(f'Non-blocking - failed to connect...')
        return

    logging.info(f'Non-blocking - connected...')
    s.setblocking(False)

    inputs = [s]
    outputs = [s]
    
    while inputs:
        logging.info(f'Non-blocking - waiting...')
        readable, writable, exceptional = select.select(inputs, outputs, inputs, 0.5)

        for s in writable:
            logging.info(f'Non-blocking - sending...')
            data = s.send(b'Hello\r\n')
            logging.info(f'NOn-blocking - sent: {data}')
            outputs.remove(s)

        for s in readable:
            logging.info(f'Non-blocking - reading...')
            data = s.recv(1024)
            logging.info(f'Non-blocking - data : {len(data)}')
            logging.info(f'Non-blocking - closing...')
            s.close()
            inputs.remove(s)
            break

        for s in exceptional:
            logging.info(f'Non-blocking - Error...')
            inputs.remove()
            outputs.remove()
            break


def main():
    # create_blocking('google.com', 80)
    create_nonblocking('voidrealms.com', 80)

if __name__ == '__main__':
    main()
    