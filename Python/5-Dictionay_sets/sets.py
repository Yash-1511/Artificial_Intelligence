a = {1,3,4}
print(a)
b = {1,2,3,4,2} 
print(b) #it will give {1,2,3,4}
#not accept duplicatte value
#an empty set created using below :
c =set()
print(type(c))
c.add(2)
c.add(3)
c.add((4,5,3))#you can add tuple in set but not dictionary and list
print(c)
print(len(b))
c.remove(2)
print(c)