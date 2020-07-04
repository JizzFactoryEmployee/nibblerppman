import time
import subprocess
import inotify.adapters

def ATOMrunner():
    while 1 <2: 
        i = inotify.adapters.Inotify()
        i.add_watch(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/ATOM/1m')
        events = i.event_gen(yield_nones=False, timeout_s=1)
        a = list(events)
        if a == []:
            pass
        if a != []:
            b = str(a)
            b.split(',')
            if 'ATOM' in b:
                print('ACTIVATING ATOMPUSHBOT')
                ATOM = subprocess.Popen(['python', '/home/nibbler/nibblerppman/nibbler/trading/collectors/testfiles/ATOMMAGIC.py'], shell=False)

ATOMrunner()
