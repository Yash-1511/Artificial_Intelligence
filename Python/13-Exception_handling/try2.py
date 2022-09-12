try:
    a = int(input("Enter your number1: "))
    b = int(input("Enter your number2: "))
    c = a/b
    print(c)
except ValueError as e:
    print("Enter valid arguments")
except ZeroDivisionError as e:
    print("Cannot Divide with 0")
except Exception as e:
    print("Other Exception error")
print("Thankyou for using this calculator")
