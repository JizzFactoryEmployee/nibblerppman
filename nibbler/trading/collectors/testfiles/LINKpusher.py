import time
import subprocess
import inotify.adapters

def LINKrunner():
    while 1 <2: 
        i = inotify.adapters.Inotify()
        i.add_watch(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/LINK/1m')
        events = i.event_gen(yield_nones=False, timeout_s=1)
        a = list(events)
        if a == []:
            pass
        if a != []:
            b = str(a)
            b.split(',')
            if 'LINK' in b:
                print('ACTIVATING LINKPUSHBOT')
                LINK = subprocess.Popen(['python', '/home/nibbler/nibblerppman/nibbler/trading/collectors/testfiles/LINKMAGIC.py'], shell=False)

LINKrunner()
