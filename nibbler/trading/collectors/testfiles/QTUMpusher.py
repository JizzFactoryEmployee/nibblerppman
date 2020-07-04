import time
import subprocess
import inotify.adapters

def QTUMrunner():
    while 1 <2: 
        i = inotify.adapters.Inotify()
        i.add_watch(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/QTUM/1m')
        events = i.event_gen(yield_nones=False, timeout_s=1)
        a = list(events)
        if a == []:
            pass
        if a != []:
            b = str(a)
            b.split(',')
            if 'QTUM' in b:
                print('ACTIVATING QTUMPUSHBOT')
                QTUM = subprocess.Popen(['python', '/home/nibbler/nibblerppman/nibbler/trading/collectors/testfiles/QTUMMAGIC.py'], shell=False)

QTUMrunner()
