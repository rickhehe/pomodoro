import time
from datetime import timedelta, datetime


def pomodoro(mode, scale):

    start_time = datetime.now() 
    duration = timedelta(seconds = standard_time[mode] * 60 * scale)
    end_time = start_time + duration

    print(i.replace('_', ' '), 'starts at:', start_time)
    print(i.replace('_', ' '), 'ends at:', end_time)

    time.sleep(duration.seconds)
    print(datetime.now(), ', ', message[mode])

#Set parameters.
standard_time = {'work':25, 'short_break':5, 'long_break':15}
message = {'work': 'take a break', 'short_break': 'go back to work', 'long_break': 'go back to work'}

#basic test
for i in ['work', 'short_break', 'long_break']:
    pomodoro(i, scale = 0.1)
