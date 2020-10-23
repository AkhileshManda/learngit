n=int(input("Enter any number"))
prod=1
if(n<0):
    print("No factorial for negative number")

if(n>0):
    for i in range(n):
        prod=prod*(n-i)

else:
    print("1")

print(prod)
    
