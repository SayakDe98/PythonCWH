myDict = {
    "Fast": "In a Quick Manner",
    "Harry":"A Coder",
    "Marks" : [1,2,5],
    "anotherdict":{"harry":"Player"}    #Nested dictionary
}

print(myDict["Fast"])   #prints the value corresponding to the key Fast
print(myDict["Harry"])
print(myDict["Marks"])
myDict["Marks"]=[45,78]
print(myDict["Marks"])
print(myDict["anotherdict"]["harry"])   #Accessing a nested dictionary

#we can't have duplicate values in dictionary , we can have overwritten values atmost.


