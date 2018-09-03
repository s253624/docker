import time

fi = open("test.conf", "r")
st = str(fi.read())
while(1):
    print(st)
    time.sleep(0.5)

