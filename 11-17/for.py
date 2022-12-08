#© 2022 11.17 WorkSquash

lista=[21,54,65,43,66,44,23,64]
print(lista)

for szam in lista:
    print(szam)

lista2=["Macska","Egér","Kutya","Oroszlán","Tigris"]

for allat in lista2:
    print(allat,"-->",len(allat),"db betűből áll")

for f in range(-5,5,2):
    print(f)

tol=int(input("Mettől?: "))
ig=int(input("Meddig?: "))


osszeg=0
db=0

big_list=[]

while ig<tol:
    ig=int(input("Meddig?: "))

for g in range(tol,ig+1):
    if g%2==0:
        osszeg=osszeg+g
        db=+1
        print(g)
        big_list.append(g)
if db<=0:
    print("Nincsenek Számok")
else:
    print('A páros számok átlaga: ', osszeg/db)

print('A páros számok összege: ',osszeg)
print(big_list)


