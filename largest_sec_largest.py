list = [123,12,432,45,1,14,12,432]
t= max(list)
for i in range(len(list)):
    if (t == list[i]):
        break
print(t," ",i)
a = t
list.remove(t)
t= max(list)
for i in range(len(list)):
    if (t == list[i] and a!=t):
        break
print(t," ",i)
