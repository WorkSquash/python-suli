szam1=int(input('Add meg az 1. szám erékét!'))
szam2=int(input('Add meg az 2. szám erékét!'))

while szam1 != szam2:
    if szam1 > szam2:
        szam1=szam1-szam2
    if szam2> szam1:
        szam2=szam2-szam1

print('A legnayobb közös osztó: ', szam1)