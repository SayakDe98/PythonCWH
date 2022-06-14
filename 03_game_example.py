class Remote():
    pass

class Player:#encapsulation
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass

remote1=Remote()    #for objects choose a variable and assign it to classname
player1=Player()    #player1 is object,Player() is the class

if(remote1.isLeftPressed()):#abstraction
    player1.moveLeft()
if(remote1.isRightPressed()):
    player1.moveRight()
if(remote1.isTopPressed()):
    player1.moveTop()