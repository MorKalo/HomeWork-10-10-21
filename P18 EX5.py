name=input('plz insert a name')
salary=int(input('plz insert a salary'))
tax=0
if salary<120000: #אם לא, חישוב לפי מדרגות 4,5
    if salary<46000:#אם לא חישוב לפי מדרגה 3
        if salary<23000: #אם לא חישוב לפי מדרגה 2
            tax=salary*0.1
        else:
            tax=salary-23000
            tax=tax*0.2
            tax=2300+tax
    else:
        tax = salary - 46000
        tax = tax * 0.3
        tax = 6900 + tax
elif salary<220000:
    tax = salary - 120000
    tax = tax * 0.4
    tax = 28100 + tax
else:
    tax = salary - 220000
    tax = tax * 0.5
    tax = 68100 + tax
print(name,'need to pay',tax,'NIS for tax')