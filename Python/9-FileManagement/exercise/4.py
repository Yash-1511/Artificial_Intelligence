f = open("donkey.txt","r")
d = f.read().lower()
f.close()
f1= open("donkey.txt","w")
f1= f1.write(d.replace("donkey","#####"))
# f1.close()