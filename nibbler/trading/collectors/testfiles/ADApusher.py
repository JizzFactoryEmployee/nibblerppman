import time
import subprocess
import inotify.adapters

def ADArunner():
    while 1 <2: 
        i = inotify.adapters.Inotify()
        i.add_watch(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/ADA/1m')
        events = i.event_gen(yield_nones=False, timeout_s=1)
        a = list(events)
        if a == []:
            pass
        if a != []:
            b = str(a)
            b.split(',')
            if 'ADA' in b:
                print('ACTIVATING ADAPUSHBOT')
                ADA = subprocess.Popen(['python', '/home/nibbler/nibblerppman/nibbler/trading/collectors/testfiles/ADAMAGIC.py'], shell=False)

ADArunner()
