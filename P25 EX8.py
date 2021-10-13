num=int(input('plz insert a num'))
temp=num
while num>0:
    if temp>num:
        temp=num
    num = int(input('plz insert a num'))
if temp>0:
    print('The lowest positive value is', temp)
else:
    print ('No positive value typed')
