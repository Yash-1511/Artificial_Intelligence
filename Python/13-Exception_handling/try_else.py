try:
    a = int(input("Enter your number1: "))
    b = int(input("Enter your number2: "))
    c = a/b
    print(c)
except ValueError as e:
    print("please enter valid value")
except ZeroDivisionError as e:
    print("cannot divide with 0")
else:
    print("We are succesfull")