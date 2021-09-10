#python script to remove leading spaces#
s1=input("enter a string : ")
l1=list(s1)
for e in range(len(l1)):
    if(l1[e]!=" "):
        print(l1[e],end="")
