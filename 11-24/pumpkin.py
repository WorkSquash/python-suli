import random 

ossz=0

max=-11

lista=[]

for f in range (random.randint(1,1000)):

    szam=random.randint(-1000,1000)

    ossz=ossz+szam

    if szam > max:

        max=szam


print ('A számok összege: ', ossz)
print ('A számok átlaga: ', ossz/f)
print ('A számok drabszáma: ', f+1)
print ('A legnagyobb szám: ', max)