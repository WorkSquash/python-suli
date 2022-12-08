#© 2022 11.03 WorkSquash

szam=int(input("Kérek egy számot:"))
min=szam
max=szam
maxi=1
mini=1
db=0

while szam!=0:
    if szam>max:
        max=szam
        maxi=db
    if szam<min:
        szam=min
        mini=db
    szam=int(input("Kérek egy számot:"))
print('A legkisebb beolvasott szám: ', min, "a", mini, "indexen található!")
print('A legnagyobb beolvasott szám: ', max, "a", maxi, "indexen található!")