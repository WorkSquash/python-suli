#© 2022 09.29 WorkSquash

import random

oszt=random.randint(2,10)

msg = 'A osztó véletlen szerűen van kivásztva 2 és 10 között!'

a=int(input('Kérem írjon be egy számot:'))

if a % 3 == 0:
    print('A szám osztható 3-mal:', a )

if a%oszt == 0:
    print(msg)
    print('A szám osztható az osztóval')
    print(a,'/', oszt, '=', 0)
    
else:
    print(msg)
    print('A szám nem osztható az osztóval')
    print(a,'/', oszt, '!=', 0)