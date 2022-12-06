import random

db=0
szam=random.randint(0,100)

while szam%7 != 0:
    szam=random.randint(0,100)
    db=db+1
    print(szam)
print("A generálások száma: ", db)