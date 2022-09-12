class Employee: #employee class
    company="Amazon" #class /member variable
    def printdata(self):  #class method
        print(f"Employee name is:{self.name}")
        print(f"Company name is:{self.company}")

yash = Employee() #object 
yash.name="yash" #instance variable
# yash.company="Google"
# Employee.company="Intitute" #changing class attribute
yash.printdata()