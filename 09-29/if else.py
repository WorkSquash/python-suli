#© 2022 09.29 WorkSquash

import random

szam=random.randint(0,100)
if szam == 0:
    print('A szám nulla:',szam)

#if szam %2 == 0:
#    print('A szám páros:',szam)

elif szam %2 == 0:
    print('A szám páros:',szam)

else: 
    print('A szám nem páros:', szam)

print('Vége')