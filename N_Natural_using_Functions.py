def nnatural(n):
    sum =0
    while n != 0:
        sum = sum + n
        n = n -1
    return sum

a = int(input("Enter the number : "))
print("Answer is : ", nnatural(a))
