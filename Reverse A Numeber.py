x = int(input("Enter a number : "))
n = x
sum = int(0)
while n!=0 :
    t = n % 10
    sum = sum*10 + t
    n = int(n/ 10)
print("Reversed order : ",sum)
