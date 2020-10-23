def prime(n):
    flag=0
    for i in range(1,n+1):
        if(n%i==0):
            flag+=1
    if(flag==2):
        return 1
    else:
        return 0
            
m=int(input("Enter maximum value for sum"))
n=int(input("Enter minimum value in range"))

s=0

for i in range(n,m+1):
    if(prime(i)==1):
        s=s+i

print(s)
