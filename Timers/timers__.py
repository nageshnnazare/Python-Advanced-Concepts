#Timers
# Execute code at timed intervals

import time
from threading import Timer

def display(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))

#Basic timer
def run_once():
    display('Run Once : ')
    t = Timer(5, display, ['Timeout:'])
    t.start()

run_once()
print('Waiting ...')

#Interval Timer
# Wrap it into class

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
        print('Done')

timer = RepeatTimer(1, display, ['Repeating '])
timer.start()
print('Treading Started ')
time.sleep(10) # suspend execution 
print('Threading finished ')

timer.cancel()