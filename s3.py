name=[]
age=[]
gender=[]
location=[]

flag=0

no= int(input("Enter number of customers :"))

for i in range(no):
    n=input("Enter name : ")
    name.append(n)
    a=input("Enter age : ")
    age.append(a)
    g=input("Enter gender : ")
    gender.append(g)
    l=input("Enter location : ")    
    location.append(l)

s = input("Enter loacation to search for : ")

for i in range(no):
    if(location[i]==s):
        flag=1
        print(name[i])
        print(age[i])
        print(gender[i])

    else:
        flag=0

if(flag==0):
    print("No customer found in location")


        
        
