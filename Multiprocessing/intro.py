# Intro to Multiprocessing
# multiple processes running the same script
# Each processes has its own memory space and its own threads

import logging
import multiprocessing
from multiprocessing import process
import time

#Process starting fn
def run(num):
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    time.sleep(num*2)
    logging.info(f'Finished {name}')

#Basic process usage
def main():
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    processes = []
    for x in range(5):
        p = multiprocessing.Process(target=run, args=[x], daemon=True)
        processes.append(p)
        p.start()

    # Wait for the processes to finish
    for p in processes:
        p.join()

    logging.info(f'Finished {name}')

logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == '__main__':
    main()
    