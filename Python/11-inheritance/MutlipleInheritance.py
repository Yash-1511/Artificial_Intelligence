class Base1:
    def showdata(self):
        print("I am father")
    def addition(self,a,b):
        return a+b
class Base2:
    def showdata1(self):
        print("I am mother")
class derived(Base1,Base2):
    def show(self):
        print("I am yash parmar")

yash = derived()
yash.show()
s = yash.addition(10,20)
print("sum is: ",s)
yash.showdata()
yash.showdata1()