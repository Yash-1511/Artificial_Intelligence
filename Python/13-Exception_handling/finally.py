try:
    a = int(input("Enter your number1: "))
    b = int(input("Enter your number2: "))
    c = a/b
    print(c)
except ValueError as e:
    print("please enter valid value")
except ZeroDivisionError as e:
    print("cannot divide with 0")
    print(e)
    exit() #if program is exit however finally will run 
finally:
    print("We are done")
print("this is will not run") #this is will not run if program is exit()