def absolutevalue(num):
    """
    This function returns absolute value
    """
    if num<0:
        num = num * -1
    return num

a = float(input("Enter any number : "))
print(absolutevalue(a))
print(absolutevalue.__doc__)
