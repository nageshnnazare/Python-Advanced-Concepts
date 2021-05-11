#Async code
#Async runs in the same thread
'''
Async uses CoRoutines which run on the same thread
"async" and "await"
'''
import logging
import multiprocessing
import threading
import time
import asyncio
import random

logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

# Functions
def display(msg):
    threadname = threading.current_thread().name
    procname = multiprocessing.current_process().name

    logging.info(f'{procname}/{threadname} : {msg}')

async def work(name):
    display(name + ' starting')
    #do something
    await asyncio.sleep(random.randint(1,10))
    display(name + ' finished')

async def run_async(max):
    tasks = []
    for x in range(max):
        name = 'Item ' + str(x)
        tasks.append(asyncio.ensure_future(work(name)))

    await asyncio.gather(*tasks)

def main():
    display('Main started')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_async(50))
    # loop.run_forever()

    loop.close()

    display('Main Finished')


if __name__ == '__main__':
    main()
    