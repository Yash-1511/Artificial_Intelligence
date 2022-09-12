def openfile(filename):
    try:
        f=open(filename,"r")
        print(f.read())
    except FileNotFoundError as e:
        print(f"{filename} not found")

openfile("1.txt")
openfile("2.txt")
openfile("3.txt")
    