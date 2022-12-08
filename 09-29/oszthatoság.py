#© 2022 09.29 WorkSquash

import random

num=random.randint (1,100)

if num % 2 == 0 and num % 3 ==0:
    print(num)
    print('A szám osztható 2-vel és 3-mal is.')

elif num % 2 == 0 or num % 3 ==0:
    print(num)
    print('A szám osztható 2-vel vagy 3-mal.')
    if num % 2 ==0:
        print('A szám osztható 2-vel de 3-mal nem.')
    else:
        print(num)
        print('A szám nem osztható 2-vel de 3-mal igen.')

elif num % 2 == 0 and num % 3 !=0:
    print(num)
    print('A szám osztható 2-vel de 3-mal nem.')

elif num % 2 != 0 and num % 3 ==0:
    print(num)
    print('A szám nem osztható 2-vel de 3-mal igen.')

else:
    print(num)
    print('A szám osztható nem 2-vel és 3-mal sem.')
