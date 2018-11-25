import time
from datetime import timedelta, datetime

#Scale is to reduce waiting time when testing. Set it to 1 unless testing.
def pomodoro(mode, scale = 0.05):
    start_time = datetime.now() 
    duration = timedelta(seconds = standard_time[mode] * 60 * scale)
    end_time = start_time + duration

    print(abbr[mode], 'starts at:', start_time.strftime('%X'))
    print(abbr[mode], 'ends at:', end_time.strftime('%X'))

    time.sleep(duration.seconds)
    print(datetime.now(), ', ', end_message[mode])

#Set parameters.
standard_time = {'w':25, 's':5, 'l':15}
end_message = {'w': 'take a break', 's': 'go back to work', 'l': 'go back to work'}
abbr = {'w':'work', 's':'short_break', 'l':'long_break'}

while 1:
    wsl = input('what are you going to do? w for work, s for short_break, l for long_break: ').lower()

    if wsl.startswith('w') or wsl.startswith('s') or wsl.startswith('l'):
        pomodoro(wsl[:1])
    elif wsl.startswith('q'):
        break
    else:
        print('typo? q for quit')
