#Simple Producer and Consumer Problem
# demonstrates queues and events with locks

import random
import threading
from threading import Thread
import multiprocessing
from queue import Queue
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

#Functions
def display(msg):
    threadname = threading.current_thread().name
    procname = multiprocessing.current_process().name

    logging.info(f'{procname}-{threadname} : {msg}')

#Producer
def create_work(queue, finished, max):
    finished.put(False)
    for x in range(max):
        v = random.randint(1, 100)
        queue.put(v)
        display(f'Producing {x} : {v}')
    finished.put(True)
    display(f'Finished P')

#Consumer
def perform_work(work, finished):
    counter = 0
    while True:
        if not work.empty():
            v = work.get()
            display(f'Consuming {counter} : {v}')
            counter += 1
        else:
            q = finished.get()
            if q == True:
                break
        display(f'Finished C')

#Main
def main():
    max = 50
    work = Queue()
    finished = Queue()

    producer = Thread(target=create_work, args=[work, finished, max], daemon=True)
    consumer = Thread(target=perform_work, args=[work, finished], daemon=True)

    producer.start()
    consumer.start()

    producer.join()
    display(f'Producer has Finished')

    consumer.join()
    display(f'Consumer has Finished')

    display(f'Main finished')

if __name__ == '__main__':
    main()
    
