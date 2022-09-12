from typing import overload


class Base:
    @staticmethod
    def greet():
        print("Hello Everyone")
class Derived(Base):
    @staticmethod
    def greet1():
        print("Good Morning")

obj = Derived()
obj.greet()