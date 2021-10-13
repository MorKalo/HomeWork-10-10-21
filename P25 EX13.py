x=int(input('plz insert a num'))
digit=int(input('plz insert a digit'))
i=0
while x!=0:
#    print(x%10)
    i2=x%10
    print(i2)
    if digit==i2:
        i=i+1
    x=x/10
print ('the DIGIT',digit,'is', i,'in the number that you input')