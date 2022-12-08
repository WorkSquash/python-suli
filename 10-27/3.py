#© 2022 10.27 WorkSquash

osszeg=0
db=0
szam=int(input('Adj meg egy egész számot!'))

while szam!=0:
    szam=int(input('Adj meg egy  új egész számot!'))

print('A szám összege: ',osszeg)

if db>0:
    atl=osszeg/db
    
else:
    atl="Nincsenek számok"

print("A számok Átlaga:",atl)