def binary(n):
    if n==0 :
        return 
    binary(n//2)
    print(n%2,end="")
def octal(n):
    if(n==0):
        return
    octal(n//8)
    print(n%8,end="")
def hexadec(n):
    if(n == 0 or n == 1):
        return
    else:
        hexadec(n//16)
        a = n%16
        if(a<10):
            print(a,end="")
        if(a == 10):
            print("A",end="")
        if(a == 11):
            print("B",end="")
        if(a == 12):
            print("C",end="")
        if(a == 13):
            print("D",end="")
        if(a == 14):
            print("E",end="")
        if(a == 15):
            print("F",end="")
a = int(input("Enter the number : "))
binary(a)
print()
octal(a)
print()
hexadec(a)
