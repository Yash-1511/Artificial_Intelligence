class Programmer:
    company="Microsoft"
    def printdata(self):
        print(f"name is: {self.name}")
        print(f"designation is:{self.designation}")
        print(f"salary is:{self.salary}")

yash = Programmer()
yash.name="yash"
yash.designation="web developer"
yash.salary=10000
yash.printdata()