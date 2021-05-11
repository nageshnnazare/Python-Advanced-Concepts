#Thread basics
"""
Move a function to multiple threads &
Wait for all threads to complete
"""
import logging
from threading import Thread
import time
import random

#Function to perform work
def longtask(name):
    max = random.randrange(1,10)
    logging.info(f'Task: {name} performing {str(max)} times ')
    for x in range(max):
        logging.info(f'Task {name} : {x}')
        time.sleep(random.randrange(1,3))
    logging.info(f'Task: {name} : complete')


def main():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Starting')
    # longtask('main')

    #Run it as thread:
    threads = []
    for x in range(10):
        t = Thread(target=longtask, args=['thread' + ' ' + str(x)])
        threads.append(t)
        t.start()

    # Wait till all threads are finished
    for t in threads:
        t.join()

    logging.info('Finished all threads')


if __name__ == '__main__':
    main()
    
