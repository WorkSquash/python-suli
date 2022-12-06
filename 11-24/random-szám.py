import random 

szam=random.randint(0,100)

pro=5

input('Ha egynél nagyobb számot írsz be, akkor a játék automatikusan véget ér.')

csal=int(input('Csalások bekapcsolása? [0-1]'))



while csal==1 or csal==0 and pro!=1:
    csal=int(input('Biztosan bekapcsolod a csalásokat? [0-1]'))
    if csal==1:
        print('Csalás bekapcsolva.')
        print(szam)

        tipp=int(input('Adja meg a tippjét! [0-100]'))

        pro=5
        while pro !=1:
            if tipp>szam:
                pro=pro-1
                print('A tipp nagyobb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=int(input('Adja meg a tippjét! [0-100]'))
        
            elif szam>tipp:
                pro=pro-1
                print('A tipp kisebb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=int(input('Adja meg a tippjét! [0-100]'))
        
        

            else:
                print('Eltaláltad!')
                pro=1
                print('A szám', szam, 'volt!')

    elif csal==0:
        print('Csalás kikapcsolva.')

        tipp=int(input('Adja meg a tippjét! [0-100]'))

        pro=5
        while pro !=1:
            if tipp>szam:
                pro=pro-1
                print('A tipp nagyobb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=int(input('Adja meg a tippjét! [0-100]'))
        
            elif szam>tipp:
                pro=pro-1
                print('A tipp kisebb mint a szám!')
                print('Probáld újra')
                print(pro,'próbálkozása maradt!')
                tipp=int(input('Adja meg a tippjét! [0-100]'))
        
        

            else:
                print('Eltaláltad!')
                pro=1
                print('A szám', szam, 'volt!')
print('Játék vége!')
print('A szám', szam, 'volt!')