#© 2022 11.24 WorkSquash

import random 

szam=round(random.uniform(0, 10), 2)

pro=0
input('Ha egynél nagyobb számot írsz be, akkor a játék automatikusan véget ér.')

csal=int(input('Csalás bekapcsolása? [0-1]'))



while pro!=1:
    csal=int(input('Biztosan bekapcsolod a csalást? [0-1]'))
    if csal==1 and csal!=0:
        print('Csalás bekapcsolva.')
        print(szam)

        pro=int(input('Adja meg a próbálkozások számát!:'))

        tipp=float(input('Adja meg a tippjét! [0-10] (PL:9.99)'))

        while pro !=1:
            if tipp>szam:
                pro=pro-1
                print('A tipp nagyobb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=float(input('Adja meg a tippjét! [0-10] (PL:9.99)'))
        
            elif szam>tipp:
                pro=pro-1
                print('A tipp kisebb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=float(input('Adja meg a tippjét! [0-10] (PL:9.99)'))
        
        

            else:
                print('Eltaláltad!')
                pro=1
                #print('A szám', szam, 'volt!')

    elif csal==0 and csal!=1:
        print('Csalás kikapcsolva.')

        pro=int(input('Adja meg a próbálkozások számát!:'))
        
        tipp=float(input('Adja meg a tippjét! [0-10] (PL:9.99)'))

        while pro !=1:
            if tipp>szam:
                pro=pro-1
                print('A tipp nagyobb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=float(input('Adja meg a tippjét! [0-10] (PL:9.99)'))
        
            elif szam>tipp:
                pro=pro-1
                print('A tipp kisebb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=float(input('Adja meg a tippjét! [0-10] (PL:9.99)'))
        
        

            else:
                print('Eltaláltad!')
                pro=1
                #print('A szám', szam, 'volt!')
print('Játék vége!')
print('A szám', szam, 'volt!')
