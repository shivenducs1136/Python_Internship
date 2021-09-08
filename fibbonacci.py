x = int(input("Enter the end point of fibbonacci : "))
a = int(0)
b = int(1)
next = 0
print(a,",",end=" ")
print(b,",",end=" ")
for i in range(0,x+1):
    next = a + b
    a = b
    b = next
    print(b,",",end=" ")
        
