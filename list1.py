list=[10,20,33,40,50]
sum = 0
for i in list :
    sum = sum + i
    if i%2==0:
        print(i,"is Even")
    else:
        print(i,"is Odd")

print("Sum is : ",sum)
