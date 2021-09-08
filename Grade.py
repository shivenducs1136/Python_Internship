print("Enter the Marks of the subject in 100 ")
sub1 = float(input("Enter the marks of sub1 : "))
sub2 = float(input("Enter the marks of sub2 : "))
sub3 = float(input("Enter the marks of sub3 : "))
sub4 = float(input("Enter the marks of sub4 : "))
sub5 = float(input("Enter the marks of sub5 : "))

per = (sub1+sub2+sub3+sub4+sub5)/5
print("Your Percentage is : ",per)
print ("And your Grade is: ")
if per>= 75:
    print("A Grade")
elif 60<=per<75:
    print("B Grade")
elif(55<=per<60):
    print("C Grade")
elif(45<=per<55):
    print("D Grade")
elif(30<=per<45):
    print("E Grade")
else :
    print("FAIL")
    
