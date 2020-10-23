n=int(input("total no. of students : "))
c=1
s=0
mark=0
while(c<=n):
    mark=int(input("Enter mark : "))
    s=s+mark
    c=c+1
print(s/n)
