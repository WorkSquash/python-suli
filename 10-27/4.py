#© 2022 10.27 WorkSquash

import random

osszeg=0
db=0
szam=random.randint(-10,10)

while szam!=0:

   db=db+1
   osszeg=osszeg+szam

print('A számok összege: ',osszeg)

if db>0:
    atl=osszeg/db

else:
    atl="Nincsenek számok"

print("A számok átlaga:",atl)