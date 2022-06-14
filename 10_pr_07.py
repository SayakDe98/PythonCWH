#strip() function
this = "    Sayak is good       "
print(this.strip())

def remove_and_split(string,word):
    newStr=string.replace(word," ") #using this we replaced word with blank space
    return newStr.split()

n=remove_and_split(this,"Sayak")
print(n)