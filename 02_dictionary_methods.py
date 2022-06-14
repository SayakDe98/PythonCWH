myDict = {
    "fast": "In a Quick Manner",
    "harry":"A Coder",
    "marks" : [1,2,5],
    "anotherdict":{"harry":"Player"},    #Nested dictionary
    1:2
}
print(myDict.keys())    #print keys of myDict in a list form
print(type(myDict)) #myDict's type is dict class
print(list(myDict)) #converts dictionary into list
print(type(list(myDict)))
print(myDict.values())  #prints all the values of the dictionary myDict
print(myDict.items())   #prints the keys as well as values of myDict,i.e. all the contents of key value pairs
print(myDict)
updateDict = {
    "Lovish":"Friend",
    "Shubham":"Friend",
    "Divya":"Friend",
    "Harry":"Dancer"    #if we update the dictionary with a key which is already present then after we join both these dictionaries the new dictionary gets updated
}
myDict.update(updateDict)   #updates the dictionary by adding key-value pairs from updateDict
print(myDict)
#in both the ways we can display value corresponding to key
print(myDict.get("harry"))  

print(myDict["harry"])
#in the first way(i.e. .get() method) if we put a key which is absent then it will display None,
#in the second way(i.e. using square bracket) if we put a key which is absent then it will display error

