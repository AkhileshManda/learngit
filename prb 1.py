basic_pay=float(input("Enter basic salary of employee"))
DA = 0.8*(basic_pay)
HRA=0.3*(basic_pay)
PF=0.12*(basic_pay)

salary= basic_pay+DA+HRA-PF

print("DA is :",DA)
print("HRA is :",HRA)
print("PF is :",PF)
print("Total salary is ",salary)
