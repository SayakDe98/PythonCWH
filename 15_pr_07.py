n = 3
for i in range(n):
    #end="" means won't print new line
    print(" " * (n-i-1) , end="")#Spaces before *
    print("*" * (2*i+1) , end="")#Number of stars
    #print(" " * (n-i-1))#to count number of spaces after * but it is redundant
    print()#prints a new line, so that control can reach next line