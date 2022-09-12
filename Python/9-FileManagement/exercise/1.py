f = open("exercise\poem.txt","r")
d = f.read()
print(d)
if "twinkle" in d:
    print("I found twinkle word in poem.txt")
else:
    print("I can't find word")
f.close()