def reqsum(*passed):
    sum =0 
    for i in passed:
        sum = sum + i
    return sum
print(reqsum(1,2,3,4,5,6))
print(reqsum(10,20,30,40,50,60))
