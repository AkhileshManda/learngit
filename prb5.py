minutes=int(input("Enter no. of minutes used"))
hrs =  int(input("Enter no. of hours used"))

amt = 0

while(int(hrs)>7 or int(hrs)<0):
    print("Invalid entry, try again")
    hrs= input()

while(minutes>60 or minutes<0):
    print("Invalid entry, try again")
    minutes= input()


if(hrs>=5):
    amt = 200 + (hrs-5)*50 + (minutes)*1

elif(hrs<5):
    amt = (hrs)*50


print("Total cost is : ",amt)
