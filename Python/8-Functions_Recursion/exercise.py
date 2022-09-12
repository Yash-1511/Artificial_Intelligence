#1. write a program using functions to find greatest of three numbers.
def greatest(n1,n2,n3):
    if n1>n2 and n1>n3:
        print("n1 is greatest")
    elif n2>n1 and n2>n3:
        print("n2 is greatest")
    else:
        print("n3 is greatest")
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))
greatest(n1,n2,n3)
#3. how do you prevent a python print() function to print a new line at the end.
print("hello",end=" ")
print("world")
#4. write a recursive function to calculate the sum of first n natural numbers.
def natural(n):
    if n==1:
        return 1
    else:
        return n + natural(n-1)
n = int(input("Enter the number: "))
print("sum of n natural numbers: ",natural(n))
#write a program to using function print multiplication table of a given number.
def multiplication(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
multiplication(10)