class Employee:
    company="Google"
    salary=10000
    def changesalary(self,sal):
        self.__class__.salary=sal# dunder class
    @classmethod
    def changesalary(cls,sal):
        cls.salary=sal

yash = Employee()
print("Before Changing yash's salary is: ",yash.salary)
# yash.changesalary(1000)
Employee.changesalary(100)
print("After changing yash's salary is: ",yash.salary)
print("Class variable salary value is: ",Employee.salary)
