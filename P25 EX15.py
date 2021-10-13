num=int(input('plz insert a num'))
dig=0
while num!=0 and dig!=0:
    num1=num%10
    dig = num//10
    print('dig', dig)
    print ('num1', num1)
    if dig!=num1:
        print('לא פלינדרום')
        break
    else:
        num=num%10
if num==0:
    print('פלינדרום')
