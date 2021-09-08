import math
a = int(input("Enter the value of a: " ))
b = int(input("Enter the value of b: " ))
c = int(input("Enter the value of c: " ))

root1 = (-1*b) + (math.sqrt(b**2 - (4*a*c)))
root1 = root1/(2*a)
print("First root is: ",root1)
root2 = (-1*b) - (math.sqrt(b**2 - (4*a*c)))
root2 = root2/(2*a)
print("Second root is: ",root2)


