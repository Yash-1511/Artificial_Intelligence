#1.write a prgramt to create a dictionary of hindi words with values as their english words.provide user with an option to look it up
hindi ={
    "mai": "i",
    "tum" : "you",
    "bijli" : "light"
}
print("options are: ")
print(hindi.keys())
# print("options are : "+hindi.keys())
a = input("Enter your choice: ")
print("Your english word is: ")
print(hindi[a])
#2 . write a program to input eight numbers from the user and display all the unique numbers
b = {1,1,2,3,4,34,343}
print(b)
#3. can we have set with 18(int) and 18(string) as a value in it?
#answer: yes you can
#4. length of this set
s=set();
s.add(20)
s.add(20.0)
s.add("yash")
print(len(s))
#5. s = { } what is the type 
#answer : dictionary
