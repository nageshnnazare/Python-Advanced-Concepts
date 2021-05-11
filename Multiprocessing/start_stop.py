# Processes Staring and Stoping

# the Full Life Cycle

import logging
import multiprocessing
from multiprocessing.context import Process
import time

#Worker process:
def work(msg, max):
    name = multiprocessing.current_process().name
    logging.info(f'Starting {name}')
    for x in range(max):
        logging.info(f'{name} {msg}')
        time.sleep(1)
    logging.info(f'Finished {name}')

#Main process:
def main():
    logging.info(f'Started : Main()')
    max = 2
    # max = 10
    worker = Process(target=work, args=['Working', max], daemon=True, name='Worker:>')
    worker.start()
    time.sleep(5)

    #if the process in running, stop it
    if worker.is_alive():
        worker.terminate()
    worker.join()

    #exit code == 0 -> OK, anything else means error
    logging.info(f'Finished : {worker.exitcode}')

logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == '__main__':
    main()
    