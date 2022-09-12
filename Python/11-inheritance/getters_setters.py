class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printdata(self):
        return f"First name is:{self.fname} and last name is: {self.lname}"
    @property
    def printemail(self):
        return f"{self.fname}{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        string.split("@")[0]

a = Employee("yash","parmar")
b = Employee("rohit","sharma")
a.fname="DY"
print(a.printemail)