#Daemon Threads
#Quiting when we quit the app

import logging
import threading
from threading import Timer, Thread
import time

#Test function
def test():
    threadname = threading.current_thread().name
    logging.info(f'Starting : {threadname}')
    for x in range(60):
        logging.info(f'Working : {threadname}')
        time.sleep(1)
    logging.info(f'Finished : {threadname}')

def stop():
    logging.info(f'Exiting the Application')
    exit(10)

def main():
    logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Main Thread Starting')

    #Stop in 3 sec
    timer = Timer(3, stop)
    timer.start()

    #Run a thread
    t = Thread(target=test,daemon=True)
    t.start()

    logging.info('Main Thread Finished')


if __name__ == '__main__':
    main()
    