import time
import subprocess
import inotify.adapters

def THETArunner():
    while 1 <2: 
        i = inotify.adapters.Inotify()
        i.add_watch(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/THETA/1m')
        events = i.event_gen(yield_nones=False, timeout_s=1)
        a = list(events)
        if a == []:
            pass
        if a != []:
            b = str(a)
            b.split(',')
            if 'THETA' in b:
                print('ACTIVATING THETAPUSHBOT')
                THETA = subprocess.Popen(['python', '/home/nibbler/nibblerppman/nibbler/trading/collectors/testfiles/THETAMAGIC.py'], shell=False)

THETArunner()