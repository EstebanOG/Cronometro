import time
ms=0
ss=0
mm=0
hh=0
while True:
    print(hh,":",mm,":",ss,":",ms)
    time.sleep(0.1)
    ms=ms+1
    if ms==10:
        ms=0
        ss=ss+1
    if ss==60:
        ss=0
        mm=mm+1
    if mm==60:
        mm=0
        hh=hh+1