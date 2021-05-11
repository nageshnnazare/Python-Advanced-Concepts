#Thread Locking
'''
Avoiding the dreaded race condition and deadlocks
Race condition: same resource modified by multiple threads
Deadlock: multiple threads waiting on the same resource
'''

import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random

counter = 0

def test(count):
    global counter
    threadname = threading.currentThread().name
    logging.info(f'Starting : {threadname} ')

    for x in range(count):
        logging.info(f'Count : {threadname} += {count}')

    # Work here
    # The Global interpreter lock (GIL) in action
        # counter += 1

    #Locking
        '''lock = threading.Lock()
        lock.acquire()
        # lock.acquire() # Deadlock Condition

        try:
            counter += 1
        finally:
            lock.release()
        '''

        #Locking Simplified
        lock = threading.Lock()
        with lock:
            logging.info(f'Locked : {threadname}')
            counter += 1
            time.sleep(2)


    logging.info(f'Completed : {threadname}')

def main():
    logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Starting')

    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for x in range(workers*2):
            v = random.randrange(1,5)
            executor.submit(test, v)

    logging.info(f'Counter = {counter}')
    logging.info('App Finished')

if __name__ == '__main__':
    main()
    