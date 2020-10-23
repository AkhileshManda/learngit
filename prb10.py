a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))

print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")


choice=int(input("Enter your choice :"))

while(choice<1 or choice>4):
    print("wrong choice")
    choice=int(input("Enter your choice :"))

if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)




    

    

    


           





 
 

