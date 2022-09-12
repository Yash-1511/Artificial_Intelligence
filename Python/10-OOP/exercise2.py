import math
class Calculator:
    def square(self,a):
        print(f"Square of {a} is : {a*a}")
    def cube(self,b):
        print(f"Cube of {b} is: {b*b*b}")
    def squareroot(self,c):
        print(f"Squaerroot of {c} is: {math.sqrt(c)}")
calc = Calculator()
s = int(input("enter number: "))
calc.square(s)
c = int(input("enter number: "))
calc.cube(c)
sq = int(input("enter number: "))
calc.squareroot(sq)