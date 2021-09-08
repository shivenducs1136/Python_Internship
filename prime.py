a=int(input("enter no : "))
flag = 0
for i in range(2,int(a/2)+1):
    if(a%i==0):
            print("no is not prime ")
            flag =1
            break
    
if(flag == 0):
    print("Number is Prime ")
