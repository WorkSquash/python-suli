#© 2022 11.24 WorkSquash

print("A * karakterrel befejezheted a kódót." )
szo=input('Kérek egy szót:')
hossz=len(szo)
max=hossz
maxszo=szo



while szo != "*":
    szo=input('Kérek egy új szót:')
    hossz=len(szo)

    if hossz > max:
        max=hossz
        maxszo=szo

print('a leghosszab szó:', maxszo, )
print(maxszo, ' ennyi betűböl áll :', max)