#© 2022 12.08 WorkSquash
import time

start = time.time()

A=1

while A!=0:
    A=A+1
    fut = round((time.time() - start), 10)

    print('A programindítása óta eltelt idő: ' + str(fut), 'sec')