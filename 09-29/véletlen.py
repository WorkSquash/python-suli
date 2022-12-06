import random

tort=random.random()

print('A tört értéke:', tort)

egesz=random.randint(1,20)

print('A szám értéke 1 és 20 között:', egesz)

egesz2=random.randrange(1,20,3)

print('A szám értéke 1 és 20 között, 3 lépéssel:', egesz2)

lista=[12,56,21,69,54,66,32,49]

szam=random.choice(lista)

print('Egy véletlen szám a listából:', szam)

lista_nev=["Béla", "Pista", "Laci", "Sanyi", "Elek", "Rozi", "Ákos"]

nev=random.choice(lista_nev)

print('Egy véletlen név a listából:', nev)

negativ=random.randint(-10,10)

print('A szám értéke -10 és 10 között:', negativ)