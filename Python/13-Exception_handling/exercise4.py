try:
    a=int(input("enter your number A: "))
    b=int(input("enter your number B: "))
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print("Infinite....")