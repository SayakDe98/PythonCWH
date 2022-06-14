#if the value in hiscore is less than 4 then we change value to 4
def game():
    return 4467

score=game()
with open("hiscore.txt") as f:
    hiscoreStr=f.read()
if(hiscoreStr==''):
    with open("hiscore.txt",'w') as f:
       f.write(str(score))
elif(int(hiscoreStr)<score):
    with open("hiscore.txt",'w') as f:
        f.write(str(score))