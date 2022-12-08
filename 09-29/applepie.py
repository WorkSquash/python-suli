#© 2022 09.29 WorkSquash

import random

num=random.randint (1,100)

if num % 5 == 0 and num % 4 ==0:
    print(num)
    print('A szám osztható 5-tel és 4-gyel is.')

elif num % 5 == 0 or num % 4 ==0:
    print(num)
    print('A szám osztható 5-tel vagy 4-gyel.')
    if num % 5 ==0:
        print('A szám osztható 5-tel de 4-gyel nem.')
    else:
        print(num)
        print('A szám nem osztható 5-tel de 4-gyel igen.')

elif num % 5 == 0 and num % 4 !=0:
    print(num)
    print('A szám osztható 5-tel de 4-gyel nem.')

elif num % 5 != 0 and num % 4 ==0:
    print(num)
    print('A szám nem osztható 5-tel de 4-gyel igen.')

else:
    print(num)
    print('A szám osztható nem 5-tel és 4-gyel sem.')
