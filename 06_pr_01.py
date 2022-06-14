myDict = {
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Item"
}

print("Options are",myDict.keys())
a = input("Enter the Hindi Word:")

#print("The meaning of your word is:",myDict[a])
#using alternative of above line since below line will not throw an error 
#if key is absent
print("The meaning of your word is:",myDict.get(a))