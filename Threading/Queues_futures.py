# Queues and Futures

# Getting a value from a thread

'''
Queue is like leaving a message 
A future is used for synchronizing the program execution in the concurrent
programming languages.
They describe the object that acts as a proxy for a result that is initially unknown,
usually bcoz the computation of its value is not yet complete
'''

import logging
import threading
from threading import Timer, Thread
import time
import random
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

# Queues
# use queues to pass messages back and forth
def test_queue(name, que):
    threadname = threading.current_thread().name
    logging.info(f'Starting : {threadname}')
    time.sleep(random.randrange(1, 5))
    logging.info(f'Fininshed : {threadname}')
    ret = 'Hello ' + name + ' your random number is : ' + str(random.randrange(1, 10))
    que.put(ret)

def queued():
    que = Queue()
    t = Thread(target=test_queue, args=['Bryan', que])
    t.start()
    logging.info(f'Do something on the main thread')
    t.join()
    ret = que.get()
    logging.info(f'Returned : {ret}')

# Futures
# Easier and cleaner
def test_future(name):
    threadname = threading.current_thread().name
    logging.info(f'Starting : {threadname}')
    time.sleep(random.randrange(1, 5))
    logging.info(f'Finished : {threadname}')
    ret = 'Hello ' + name + ' your random number is : ' + str(random.randrange(1, 10))
    return ret

def pooled():
    workers = 20
    ret = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers):
            v = random.randrange(1,5)
            fut = ex.submit(test_future, 'Bryan' + str(x))
            ret.append(fut)
    logging.info(f'Do something in the main thread')
    for r in ret:
        logging.info(f'Returned : {r.result()}')


def main():
    logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Main Thread Starting')
    # queued()  #Queue
    pooled()    #Future


if __name__ == '__main__':
    main()
    