num=int(input('plz insert a num'))
mun=0
while num!=0:
    dig = num%10
    mun=10*mun
    mun=mun+dig
    num=num//10
print (mun)