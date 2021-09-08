x = int(input("Enter the Number for interval : "))
for i in range(0,x+1):
    sum =int(0)
    n = int(i)
    while n>0:
        t = n %10
        sum = t**3 + sum
        n = int(n/10)
    if sum == i:
        print(i,end=",")
        
