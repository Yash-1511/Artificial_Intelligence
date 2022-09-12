def add(a, b): return a+b
def sub(a, b): return a-b
def mul(a, b): return a*b
def div(a, b): return a/b
def mod(a, b): return a % b
# Menu Driven code
print("*** Welcome to Py Calculator ***")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")
print("6. Exit")
while True:
    choice = int(input("Enter your choice: "))
    if choice in (1,2,3,4,5):
        a = int(input("Enter your number 1: "))
        b = int(input("Enter your number 2: "))
        if choice == 1:
            print("Sum is: ", add(a, b))
        elif choice == 2:
            print("Subtraction is: ", sub(a, b))
        elif choice == 3:
            print("Multiplication is: ", mul(a, b))
        elif choice == 4:
            print("Division is: ", div(a, b))
        elif choice == 5:
            print("Modulo is: ", mod(a, b))
    elif choice == 6:
        print("Thankyou!!")
        break
    else:
        print("Please Enter valid choice!")
