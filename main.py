import random
print("*"*20)
print("STONE , PAPER AND SCISSORS")
print("*"*20)

while True:
    Player_1=input("ENTER YOUR WEAPON: ").strip().lower()

    if Player_1 not in ['stone','paper','scissor']:
        print("It seems like you don't wanna paly, THANK YOU")
        break
    
    computer=random.choice(['stone','paper','scissor'])
    print(f"Computer choice: {computer}")

    if Player_1==computer:
        print("IT'S TIE")
        break

    elif Player_1=="stone" and computer=='scissor' or \
    Player_1=='paper' and computer=='stone' or \
    Player_1=='scissor' and computer=='paper':
        print("Player_1 WON!!")

    else:
        print("COMPUTER WON!!")
        break
        
