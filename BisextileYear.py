print('Tapez une année scolaire')
year=int(input())
if (year%4==0 and year%100!=0) or year%400==0:
    print("L'année " + str(year) + " est bisextile")
else:
    print('Cette année n est pas bisextile')

