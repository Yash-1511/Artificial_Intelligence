n = int(input("Enter your number: "))
l = [n*i for i in range(1,11)]
print(str(l))
f = open("table.txt","a")
f.write(str(l))
f.write("\n")
f.close()