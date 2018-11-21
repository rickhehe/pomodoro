'''
This is pretty much only a 25min timer.
start
get current time, plus 25 min, then make some noise
use input to get next action, short break or long break
'''

from datetime import datetime
import time
from datetime import date
from datetime import timedelta

def work():
    start_time = datetime.now()
    break_time = start_time + timedelta(seconds = 1*60)
    print(break_time)

    while 1:
        time.sleep(10.0) #1 min later

        current_time = datetime.now()
        time_left = break_time - current_time

        if current_time < break_time:
            print(time_left)

        else:
            print('take a break')
            break

#    print(current_time)

def short_break():
    print('take a break')
    pass

def long_break():
    pass


work()
