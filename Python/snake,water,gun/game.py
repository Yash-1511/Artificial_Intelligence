import random
def game(user,computer):
    print("Your choice: ",user)
    print("Computer choice: ",computer)
    if user==computer:
        print("Draw match")
    elif user==0 and computer==1 or user==1 and computer==2 or user==2 and computer==0:
        print("Congratulations!!")
        print("You are the winner")
    else:
        print("OOPS!!")
        print("You are the looser")
user = int(input("Enter your choice Snake(0) , water(1) and Gun(2): "))
computer = random.randint(0,2)
game(user,computer)