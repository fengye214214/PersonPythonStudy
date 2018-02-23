# python3
# threadDemo.py

import threading, time, subprocess


def takeANap():
    time.sleep(5)
    print('等等')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('结束')

threadObj1 = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],kwargs={'sep': '& '})
threadObj1.start()

timeLeft = 60

while timeLeft > 0:
    print('ok')
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1
    if timeLeft == 0:
        subprocess.Popen(['start', 'alarm.wav'], shell=True)
        break
        