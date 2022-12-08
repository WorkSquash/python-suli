#© 2022 09.22 WorkSquash

#Logikai Operátorok

a=18
b=12

x=False
y=True

x = a > b
y = a < b
z = a == b

print (a, '>', b, 'és', a, "<", b, "és",  a, "=", b, '⟶ ', x and y and z)
print (a, '>', b, 'vagy', a, "<", b, "vagy",  a, "=", b, '⟶ ', x or y or z)

x= a or b

print (a, 'vagy', b, '⟶ ', x)

x= a and b

print (a, 'és', b, '⟶ ', x)