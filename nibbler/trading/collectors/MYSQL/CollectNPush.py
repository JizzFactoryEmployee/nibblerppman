import subprocess

def runner():
    btccoll = subprocess.call(['python', r'/home/nibbler/nibblerppman/nibbler/trading/collectors/futures_collector.py'])
    print(btccoll)
    # thetacoll = subprocess.call(['python', r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/THETA/1m/THETAcollector.py'])
    # print(thetacoll)

runner()