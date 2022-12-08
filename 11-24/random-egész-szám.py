#© 2022 11.24 WorkSquash

import random 

szam=random.randint(0,100)
input('Ha egynél nagyobb számot írsz be, akkor a játék automatikusan véget ér.')

pro=0


csal=int(input('Csalás bekapcsolása? [0-1]'))



while pro!=1:
    csal=int(input('Biztosan bekapcsolod a csalást? [0-1]'))
    if csal==1 and csal!=0:
        print('Csalás bekapcsolva.')
        print(szam)
        pro=int(input('Adja meg a próbálkozások számát!:'))
        
        tipp=int(input('Adja meg a tippjét! [0-100] (Pl:36)'))
        
        while pro !=1:
            if tipp>szam:
                pro=pro-1
                print('A tipp nagyobb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=int(input('Adja meg a tippjét! [0-100] (Pl:36)'))
        
            elif szam>tipp:
                pro=pro-1
                print('A tipp kisebb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=int(input('Adja meg a tippjét! [0-100] (Pl:36)'))
        
        

            else:
                print('Eltaláltad!')
                pro=1
                print('A szám', szam, 'volt!')

    elif csal==0 and csal!=1:
        print('Csalás kikapcsolva.')
        
        pro=int(input('Adja meg a próbálkozások számát!:'))

        tipp=int(input('Adja meg a tippjét! [0-100] (Pl:36)'))

        while pro !=1:
            if tipp>szam:
                pro=pro-1
                print('A tipp nagyobb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=int(input('Adja meg a tippjét! [0-100] (Pl:36)'))
        
            elif szam>tipp:
                pro=pro-1
                print('A tipp kisebb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=int(input('Adja meg a tippjét! [0-100] (Pl:36)'))
        
        

            else:
                print('Eltaláltad!')
                pro=1
                #print('A szám', szam, 'volt!')
print('Játék vége!')
print('A szám', szam, 'volt!')
