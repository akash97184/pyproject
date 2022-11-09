from doctest import TestResults
import random

next =True
while next:
    roll= random.randint(1,6)
    print(roll)
    anotherturn=input("Do u want to roll more ? (y/n) :")
    
    if anotherturn=='y':
        continue
    else:
        break
    