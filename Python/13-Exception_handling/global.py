a = 10 #global variable
def num():
    global a #use global variable value
    a=5 #changing global variable value
    #a=5 #local variable
    print(a)#this will print 5

num()
print(a) #this will print 10