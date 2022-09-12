#1. write a program to store seven fruits in a list entered by the user.
# f1 = input("Enter fruit number 1: ")
# f2 = input("Enter fruit number 2: ")
# f3 = input("Enter fruit number 3: ")
# f4 = input("Enter fruit number 4: ")
# f5 = input("Enter fruit number 5: ")
# f6 = input("Enter fruit number 6: ")
# f7 = input("Enter fruit number 7: ")
# fruits=[f1,f2,f3,f4,f5,f6,f7]
# print(fruits)
#2. write a program to accept marks of 6 studnets and display them in a sorted manner
marks =[15,2,5,3,35,2]
marks.sort()
print(marks)
#3. check that tuple cannot be change in python
t = (1,345,3,3)
# t[0] = 12 #this will give you error because tuple are immutable
print(t)
#4. write a program to sum a list
l = [1,2,3,4]
print(l[0]+l[1]+l[2]+l[3])
print(sum(l))
#5. write a programt to count the numbers of zero in the following tuple
a=(7,0,8,0,0,9)
print(a.count(0))