#TCP Echo server
# Make a TCP server in a process that handles multiple clients
# Echoes back the data the client sent 

import logging
import multiprocessing
import socket
import select

logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

#Server
def chatserver(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info(f'Binding to {ip}:{port}')
    server.bind((ip, port))
    server.setblocking(False)
    server.listen(100)
    logging.info(f'Listening on {ip}:{port}')

    readers = [server]

    while True:
        readable, writable, err = select.select(readers, [], [], 0.5)

        for s in readable:
            try:
                if s == server:
                    client, addr = server.accept()
                    client.setblocking(False)
                    readers.append(client)
                    logging.info(f'Connected with : {addr}')
                else:
                    data = s.recv(1024)
                    if data:
                        logging.info(f'Echo: {data}')
                        s.send(data)
                    else:
                        logging.info(f'Remove: {s}')
                        s.close()
                        readers.remove(s)
            except Exception as ex:
                logging.warning(ex.args)
            finally:
                pass

def main():
    svr = multiprocessing.Process(target=chatserver, args=['localhost', 2067], daemon=True, name='Server')
    while True:
        command = input('Enter a command (start, stop) : ')
        if command == 'start':
            logging.info(f'Starting Server')
            svr.start()
        if command == 'stop':
            logging.info(f'Stopping Server')
            svr.terminate()
            svr.join()
            svr.close()
            logging.info(f'Server Stopped')
            break

        logging.info(f'Application Finished')

if __name__ == '__main__':
    main()
    