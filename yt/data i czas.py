import datetime as d
'''
teraz = d.datetime.now()

print(teraz.strftime("%H:%M %d.%m.%Y " ))
'''
import time as t

now = t.time()
timer = t.time()
i=0
while 1:
    if t.time() - now > 2:
        a=12
        i+=1
        if(i>4): break
        print(a)
        now = t.time()
    elif t.time() - timer > 5:
        b=16
        print(b)
        timer=t.time()

