#1. write a program to find greatest of four numbers entered by the user.
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))
# if num1>num2 and num1>num3 and num1>num4:
#     print("Number 1 greatest")
# elif num2>num1 and num2>num3 and num2>num4:
#     print("Number 2 greatest")
# elif num3>num1 and num3>num2 and num3>num4:
#     print("Number 3 greatest")
# elif num4>num1 and num4>num2 and num4>num3:
#     print("Number 4 greatest")
# else:
#     print("All numbers are equal")
#2.write a program to find out whether a student is pass or fail if it requires total 40% and at least 33% in each subject to pass. assume 3 subjects and take marks as an input from the user.
# sub1 = int(input("Enter first subject marks: "))
# sub2 = int(input("Enter second subject marks: "))
# sub3 = int(input("Enter third subject marks: "))
# total = ((sub1+sub2+sub3)*100)/300
# print(total)
# if total>40 and sub1>33 and sub2>33 and sub3>33:
#     print("Pass")
# else:
#     print("fail")
#3.A spam comment is defined as a text containing following keywords.
# msg = input("Enter comment: ")
# if "subscribe my channel" in msg or "make a lot of money" in msg or "buy now" in msg or "click this" in msg:
#     print("spam message")
# else:
#     print("this is not spam message")
#4. write a program to find whether a given username contains less than 10 characters or not
# username = input("Enter your name: ")
# if len(username)>10:
#     print("username contains 10 or more characters")
# else:
#     print("username contains 10 or less characters")
#5. write a programt to which finds out whether a given name is present in list or not.
l = ["yash","harry","jatin"]
name = input("enter your name: ")
if name in l:
    print("username in list")
else:
    print("username not in list")