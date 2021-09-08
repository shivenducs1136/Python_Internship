print ("General quadratic equation is in form of ax^2+bx+c ")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

D = (b**2) - (4 * a * c)
if(D<0):
    print("Solutions are imaginary")
else :
    D = D**(0.5)
    root1 = -1*b + D
    root1 = root1 / (2*a)
    root2 = -1*b - D
    root2 = root2 / (2*a)
    print("First root is : ", root1)
    print("Second root is : ",root2)
