
n=int(input('Kérek egy számot!: '))


for szam in range (1,n+1):

    prim=True

    oszto=2

    chance=0


    while oszto<=int(szam)/2 and prim:
        
        if szam%oszto==0:
        
            prim = False
        
        oszto=oszto+1

        chance=chance+0.01

    if prim==True:
        
        print('A', szam, 'prímszám!')
        chance=chance+0.01
        print(chance)
    elif prim==True and chance>=0.25:
        
        print('Ohio')
        chance=0
        print(chance)

    #else:
        
    #    print('A', szam, ' nem prímszám!')