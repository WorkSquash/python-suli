#© 2022 10.27 WorkSquash

tries=0
# the password is 2986
password=int(input('Adjon meg egy jelszót! (Pl:1234)'))
code='aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ=='
while tries!=3:
    
    if password==2986:
        print('A jelszó helyes, a kódód:', code)
        tries=3

    elif password!=2986:
        password=int(input('Adjon meg egy új jelszót!'))
        tries=tries+1
        print('Helytelen jelszó próbálja újra!')
        
    