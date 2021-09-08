num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the Second number: "))
if num1>num2:
    s = num2
else :
    s = num1
for i in range(1,s+1):
    if(num1%i==0)and(num2%i==0):
        hcf = int(i)
    
print("HCF is : ", hcf)
