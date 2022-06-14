import random

def gameWin(comp,you):
    if(comp==you):
        return None#Tie
    elif(comp=='s'):
        if(you=='w'):
            return False#You Lose
        elif(you=='g'): 
            return True#You Win
    elif(comp=='w'):
        if(you=='g'):
            return False#You Lose
        elif(you=='s'):
            return True#You Win
    elif(comp=='g'):
        if(you=='s'):
            return False#You Lose
        elif(you=='w'):
            return True#You Win


print("Computer's Turn: Snake(s) Water(w) or Gun(g)")
randNo=random.randint(1,3)#selects from1  2 or 3
#print(randNo)

if(randNo==1):
    comp='s'
elif(randNo==2):
    comp='w'
elif(randNo==3):
    comp='g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)")
a=gameWin(comp,you)

print(f"Computer chose{comp}")
print(f"You chose:{you}")
if(a==None):
    print("The game is a tie!")
elif(a):
    print("You win!")
else:
    print("You lose!")