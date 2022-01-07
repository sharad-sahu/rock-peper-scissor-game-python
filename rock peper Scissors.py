import random
lis=["rock","peper","scicor"]
while True:
    cwin=0
    uwin=0
    choice=input("do u want play this-y/n")
    if choice=="y":
        for i in range(0,5):
            user_input=int(input("""enter choice--
1.rock
2.peper
3.scicor"""))
            if user_input==1:
                uc="rock"
            elif user_input==2:
                uc="peper"
            elif user_input==3:
                uc="scicor"
            else:
                print("sorry wrong choice")
                break

            cc=random.choice(lis)

            if (uc=="rock" and cc=="scicor")or(uc=="scicor" and cc=="peper")or(uc=="peper" and cc=="rock"):
                print("_________________________________________________________________________")
                print("you win")
                uwin=uwin+1
                print("computer's choice",cc)
                print("_____________________________________________________________________________")
            elif (uc=="scicor" and cc=="rock")or(uc=="peper" and cc=="scicor")or(uc=="rock" and cc=="peper"):
                print("*********************************************************")
                print("computer win")
                cwin=cwin+1
                print("computer's choice",cc)
                print("_____________________________________________________________________________")
            elif uc==cc:
                print("_____________________________________________________________________________")
                print("round tie")
                print("_____________________________________________________________________________")
    if uwin>cwin:
        print("your are win this game")
        print("computer's total win is=",cwin)
        print("your's total win is=",uwin)
    elif uwin<cwin:
        print("computer win the game")
        print("computer's total win is=",cwin)
        print("your's total win is=",uwin)
    else:
        break
