szam=int(input("kérek egy számot: "))

while szam != 0:
    if szam/2 !=0:
        print('A szám nem páros!')
        szam=int(input("kérek egy  új számot: "))
    else:
        print('A szám páros a kód befejeződött.')
        szam=0