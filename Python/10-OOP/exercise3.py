#create a class with a class attribute a , create an object from it and set a directly using object.a=0 does this change the class attribute?
#answer = no
class A:
    a=10

obj = A()
obj.a=12
print(A.a) #this will print 10
print(obj.a) #this will print 12