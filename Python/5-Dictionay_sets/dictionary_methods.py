mydict = {
    "name" : "Yash parmar",
    "marks" : [99,24,24],
    "skills" : ("coder","programmer","hacker"),
    "anotherdict" : {'yashfavfood' : 'puff'}
}
print(mydict.keys()) #returs keys
print(type(mydict))  #return type 
print(mydict.values()) #return values
print(list(mydict.values()))
print(mydict.items()) #print the (key,value) for all the contents of the dictionary
updatedict = {
    "surname" : "parmar",
    "skills" : ("coder","programmer","hacker","datascienctist")
}
mydict.update(updatedict)
print(mydict)
print(mydict.get("name2")) #if key is not present in dictionary it will return none
# print(mydict['name2'])  #this will give you error