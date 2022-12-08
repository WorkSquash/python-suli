#© 2022 11.24 WorkSquash
letet=int(input('A lekötött összeg?'))
kamat=int(input('A kamat összege?'))
ki=letet
ev=0


while ki < letet*2:
    ki=ki*(1+kamat/100)
    ev=ev+1

print('A lekötött összeg' ,ev, 'év alatt duplázódik meg!')
print('A kifzetett összeg' ,ki,'FT')