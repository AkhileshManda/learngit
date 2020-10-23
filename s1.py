s=input()
l=len(s)
c=0
w=''
lw=0

for i in range(l):
    if(s[i]==''):
        c=c+1
    else:
        w=w+s[i]
        if(w[0]=='a' or w[0]=='e' or w[0]=='i' or w[0]=='o' or w[0]=='u'):
            print(w)

