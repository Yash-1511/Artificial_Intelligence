#1.write a programt to print multiplication table of a given number using for loop.
# n = int(input("Enter the number do you want to multiplication table: "))
# for i in range(1,11):
#     print(n," * ",i ," = ",n*i)
#2. write a programt to greet all the person names stored in a list and which starts with S.
# l = ["yash","sunil","soham","rohit"]
# for i in l:
#     if i.startswith("s"):
#         print("Hello ",i)
#3. attempt problem one using while loop.
# n = int(input("Enter the number do you want to multiplication table: "))
# i=1
# while i<=10:
#     print(n," * ",i ," = ",n*i)
#     i+=1
#4. check prime number or not
# n3 = int(input("Enter number: "))
# prime=False
# for i in range(2,n3):
#     if(n3%i==0):
#         prime=True
#         break
# if prime:
#     print("The number is not prime")
# else:
#     print("The number is prime")
#5. write a program to find the sum of first n natural numbers using while loops.
# n1= int(input("Enter number: "))
# i=1
# s=0
# while i<=n1:
#     s+=i
#     i+=1
# print(s)
#5.write a programt to calculate a factorial of a number using for loop.
# fact=1
# n2= int(input("Enter number: "))
# for i in range(1,n2+1):
#     fact*=i
# print(fact)
#10. write a program to print multiplication table of n using for loop in reverse order.
n = int(input("Enter the number do you want to multiplication table: "))
# for i in reversed(range(1,11)): 
#     print(n," * ",i ," = ",n*i)
for i in range(10,0,-1):
    print(n," * ",i ," = ",n*i)
