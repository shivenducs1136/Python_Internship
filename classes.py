class Employee:
    def __init__ (self, name, age, gender, salary, designation, department):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.designation = designation
        self.department =department
    def get_commission (self):
        return self._commission
    def set_commission(self,Rs):
        self._commission = Rs
    def intro(self):
        print("Employee name is : ",self.name)
        print("Employee gender is : ",self.gender)
        print("Employee salary is : ",self.salary)
        print("Employee designation : ",self.designation)
        print("Emplayee department : ",self.department)
    
E1 =  Employee("Abc Xyz",25,"Male",3000,"Junior Engineer","CS")
E2 =  Employee("Pqr Fgh",52,"Female",0.003,"Senior Engineer","CSIT")
E1.intro()
E2.intro()
E3 = Employee("qwerty",32,"Male",932,"Keyboard","CS")
E3.set_commission(100000)
print(E3.get_commission)
