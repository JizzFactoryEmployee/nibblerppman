import time
import subprocess
import inotify.adapters

def IOSTrunner():
    while 1 <2: 
        i = inotify.adapters.Inotify()
        i.add_watch(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/IOST/1m')
        events = i.event_gen(yield_nones=False, timeout_s=1)
        a = list(events)
        if a == []:
            pass
        if a != []:
            b = str(a)
            b.split(',')
            if 'IOST' in b:
                print('ACTIVATING IOSTPUSHBOT')
                IOST = subprocess.Popen(['python', '/home/nibbler/nibblerppman/nibbler/trading/collectors/testfiles/IOSTMAGIC.py'], shell=False)

IOSTrunner()