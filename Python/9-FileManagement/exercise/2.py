def game():
    n = int(input("Enter n: "))
    if n>18:
        f=open("exercise/score.txt","w")
        f.write("Your Score is: 1")
        f.close()
    else:
        f=open("exercise/score.txt","w")
        f.write("Your score is: 0")
        f.close()
game()
f=open("exercise/score.txt","r")
print(f.read())
f.close()