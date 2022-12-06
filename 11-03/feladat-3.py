import random
szam=random.randint(-1,1)
osszeg=szam
db=1
atlag=osszeg/db

while atlag>=0 and atlag<=2:
    szam=random.randint(-10,10)
    osszeg = osszeg + szam
    db = db + 1
    atlag=osszeg/db
    print('Hacking in progress... ', atlag, "%" ,"done.")