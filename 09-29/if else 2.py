#© 2022 09.29 WorkSquash

import random

szam=random.randint(-100,100)
if szam > 0:
    print('A szám pozitív:',szam)

elif szam < 0:
    print('A szám negatív:',szam)

else: 
    print('A szám egyenlő 0-val:', szam)

print('Vége')