class Student:
    def printdata(self,idno,name,marks):
        self.idno = idno 
        self.name = name
        self.marks = marks
        print(f"Id is:{idno}")
        print(f"name is:{name}")
        print(f"marks is:{marks}")
    def greet(self):
        print("hello user")

yash = Student()
idno = 1
name = "yash"
marks = 100
yash.printdata(idno,name,marks)
yash.greet() #Student.greet(yash)