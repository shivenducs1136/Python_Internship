lis  =  [1,23,234,32,513,23,3,13]
t = list(lis)
t.sort()
for i in range(len(lis)):
    if(lis[i] == t[0]):
        a = i
    if(lis[i] == t[1]):
        b = i
    if(lis[i] == t[len(lis)-2]):
        c = i
    if(lis[i] == t[len(lis)-1]):
        d = i
print("Smallest : ",lis[0],"at index : ",a)
print("Second smallest : ",lis[1],"at index : ",b)
print("Largest : ",lis[len(lis) -1],"at index : ",c)
print("Second Largest : ",lis[len(lis)-2],"at index : ",d)
