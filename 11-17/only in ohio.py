#© 2022 11.17 WorkSquash


n=int(input('Szám: '))

fa=1

for i in range (1,n+1):
    fa=fa*i
    print(n,"!=", fa)