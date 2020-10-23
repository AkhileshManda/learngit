dayb=int(input("Enter expected day of return : "))
dayr=int(input("Enter day of return : "))
mb=int(input("Enter expected month of return : "))
mr=int(input("Enter month of return : "))
yb=int(input("Enter expected year of return : "))
yr=int(input("Enter year of return : "))

fine = 0

if(mb==mr and yb==yr):
    if(dayb>dayr):
        fine=15*(dayb-dayr)
    else:
        fine=0

if(yb==yr):
    if(mb>mr):
        fine=500*(mb-mr)

else:
    fine=10,000

