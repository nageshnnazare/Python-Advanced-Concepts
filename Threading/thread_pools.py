# Thread pools
#reusing the existing threads because creating the threads is expensive


import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random

#Test function
def test(item):
    s = random.randrange(1,10)
    logging.info(f'Thread ({item}) : id = {threading.get_ident()}')
    logging.info(f'Thread ({item}) : name = {threading.current_thread().name}')
    logging.info(f'Thread ({item}) : sleeping for {s}')
    time.sleep(s)
    logging.info(f'Thread ({item}) : finished ')

#Main function
def main():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Starting')

    workers = 5
    items = 15
    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(test,range(items))

    logging.info('App Finished')


if __name__ == '__main__':
    main()
    

