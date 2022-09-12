str1 = "Yash parmar"
str2 = 'parmar'
str3 = '''msc.it'''
#we can write these three ways strings
#length of a string
# a = "Yash parmar , the web developer"
# print(len(a))
b="yash"
print(b[0])
#String index starts with 0
#string slicing
# print(b[0:3])
#negative indexes
print(b[:4]) #same as b[0:4]
print(b[-4:])
#string functions
#1.length functions
print(len(b))
#2.ends with function
print(b.endswith("as"))
#3.count function
print(b.count("s"))
#4. capitalize function
print(b.capitalize())
#5.find function
print(b.find('h'))
#6.replace function
print(b.replace("yash","Yash Parmar"))