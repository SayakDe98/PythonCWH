letter = '''Dear <|NAME|>,
            You are selected!
            Date: <|DATE|>'''

name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>",name)#we write letter = letter.replace("<|NAME|>",name) since strings are immutable
letter = letter.replace("<|DATE|>",date)
print(letter)