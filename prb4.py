nc=int(input("Enter no. of computer "))
nt=int(input("Enter no. of Table "))
ns=int(input("Enter no. of chairs "))
cc=float(input("Enter cost of 1 computer "))
ct=float(input("Enter cost of 1 table "))
cs=float(input("Enter cost of 1 chair "))
nw=int(input("Enter no. of hours worked "))
wh=int(input("Enter wages per hour"))

budget= (nc*cc)+(nw*wh)+(nt*ct)+(ns*cs)

print("Toatal budget should be ",budget)
