
import random
def gamewin(comp,player):
    if comp==player:
        return None
    elif comp=='s':
        if player=='p':
            return True
        elif player=='c':
            return False
    elif comp=='p':
        if player=='c':
            return True
        elif player=='s':
            return False
    elif comp=='c':
        if player=='s':
            return True
        elif player=='p':
            return False
print("Comp Turn:stone(s) paper(p) scissor(c):")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='p'
elif randno==3:
    comp='c'
player=input("player turn: stone(s) paper(p) scissor(c):")
a=gamewin(comp,player)
print(f"The comp chooses{comp}")
print(f"The player choses {player}")
if a==None:
    print("The game is tie!")
elif a:
    print("you win!")
else :
    print("you lose!")
