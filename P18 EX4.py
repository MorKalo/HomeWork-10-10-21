num=int(input('plz insert a num'))
i=1
while num>9:
    num=num//10
    i=i+1
print('The number of digits of the number you input is',i)