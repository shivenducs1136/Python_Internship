def fact(num):
    if(num == 0):
        return 1
    else:
        return (num * fact(num -1))

a = int(input("Enter the Number : "))
print("Factorial is : ",fact(a))
