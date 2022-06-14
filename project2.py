import random

randNumber=random.randint(1,100)

print(randNumber)

guesses=0

userGuess=None

while(userGuess!=randNumber):
    
    userGuess=int(input("Enter your guess:"))
    
    if(userGuess==randNumber):
        print("You guessed it right!")
    
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
    
    guesses+=1

print(f"You guessed the number in {guesses} guesses")
with open("hiscore_project_2.txt","r") as f:
    hiscore=int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score")
    with open("hiscore_project_2.txt","w") as f:
        f.write(str(guesses))