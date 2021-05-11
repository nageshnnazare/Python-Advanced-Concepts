#Communicating between processes

import logging
import time
import multiprocessing
from multiprocessing import process
from multiprocessing.context import Process
from multiprocessing.connection import Listener, Client

logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

#Worker Process
def proc(server='localhost', port=5000, password=b'password'):
    name = multiprocessing.current_process().name
    logging.info(f'{name} started')

    #start listening for connections
    address = (server,port)
    listener = Listener(address, authkey=password)
    conn = listener.accept()
    logging.info(f'{name} : connection from {listener.last_accepted}')

    #Loop for input
    while True:
        msg = conn.recv()
        logging.info(f'{name} : data in : {msg}')
        if msg == 'quit':
            conn.close()
            break
    listener.close()
    logging.info(f'{name} finished')

#main
def main():
    name = process.current_process().name
    logging.info(f'main started')

    #Set up process
    address = 'localhost' 
    port = 2923
    password = b'password'

    p = Process(target=proc, args=[address, port, password], daemon=True, name='Worker')
    p.start()

    logging.info(f'{name} waiting on the worker...')
    time.sleep(1)

    #connect to process
    dest = (address, port)
    conn = Client(dest, authkey=password)

    #command loop
    while True:
        command = input('\r\n Enter a command or type quit: \n').strip()
        logging.info(f'{name} command = {command}')
        conn.send(command)
        if command == 'quit':
            break

    #cleanup & shutdown
    if p.is_alive():
        logging.info(f'{name} terminating worker')
        conn.close()
        time.sleep(1)
        p.terminate()
    p.join()



    logging.info(f'main finished')

if __name__ == '__main__':
    main()
    
