class Monkey:
    def show(self):
        print("I am monkey")
class Person(Monkey):
    def show1(self):
        print("I am person")
class Programmer(Person):
    def show2(self):
        print("I am programmer")

p = Programmer()
p.show2()
p.show1()
p.show()