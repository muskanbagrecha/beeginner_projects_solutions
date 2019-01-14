#MUSKAN BAGRECHA
import random
def rps():
    L = ["rock", "paper", "scissors"]
    ctrcomp=0
    ctrplayer=0
    while True:
        a=int(input("Do you want to play? Type 1 for yes, 0 for no"))
        if a==0:
            print("THANK YOU")
            print("Scorecard is as follows: You={} and computer={}".format(ctrplayer, ctrcomp))
            if ctrcomp==ctrplayer:
                print("It's a tie")
            elif ctrcomp>ctrplayer:
                print("Uh-oh! You lose. Better luck next time :)")
            else:
                print("Congratulations!! You won")
            break
        else:
            choice = input("rock, paper or scissors?")
            opponent=random.choice(L)
            print("Computer: ", opponent)
            if choice == opponent:
                print("Tie")
            elif (choice=="rock" and opponent=='paper') or (choice=='paper' and opponent=='scissors') or (choice=='scissors' and opponent=='rock'):
                print("Computer gets the point")
                ctrcomp+=1
            else:
                print("You get the point")
                ctrplayer+=1
        
#MAIN
rps()
