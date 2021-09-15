class Students:
    def __init__ (self,Rollno, English,Hindi,Maths,Physics,Chemistry):
        self.Rollno = Rollno
        self.English = English
        self.Hindi = Hindi
        self.Maths = Maths
        self.Physics = Physics
        self.Chemistry = Chemistry
    def percentage(self):
        print("Marks of Roll no. : ",self.Rollno, "is : ")
        print((self.English+self.Hindi+self.Maths+self.Physics+self.Chemistry)/5)

raj = Students(int(input("Enter Your Roll number : ")),int(input("Enter English Marks : ")),int(input("Enter Hindi Marks : ")),int(input("Enter Maths Marks : ")),int(input("Enter Physics Marks : ")),int(input("Enter Chemistry Marks : ")))
raj.percentage()
