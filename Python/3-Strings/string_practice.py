#1. write a program to display a user entered name followed by good afternoon using input() function
username=input("Enter your name: ")
print("Good Afternoon " + username)
#2. write a program to fill in a letter template given below with name and date.
letter='''Dear <|name|>,
You are selcted!
Date: <|date|>
'''
name=input("Enter your name: ")
date=input("Enter your date: ")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)
#3. write a program to detect double spaces in a string
# dspace ="yash  parmar"
# print(dspace.find("  "))
#4. write a program to replace double space into single space
dspace ="yash  parmar"
dspace=dspace.replace("  "," ")
print(dspace)
#probleme 3 second method
a="yash  parmar"
print("  " in a)

