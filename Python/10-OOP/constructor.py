class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print(f"name is:{name}")
        print(f"salary is:{salary}")
    @staticmethod
    def greet():
        print("hello user")
    @staticmethod
    def morning():
        print("good morning")

yash = Employee("yash",1000)
yash.greet()
