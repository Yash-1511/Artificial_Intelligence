from typing import Mapping


def greet(name):
    print(f"Good Morning {name}")
print(__name__)
if __name__=="__main__":
    name = input("Enter your name: ")
    greet(name)