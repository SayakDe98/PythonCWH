a = {1,3,4,5}   #This is a set
print(a)
print(type(a))

#if we try to input duplicate values in a set only one of the values will be counted
a = {1,3,4,5,1}
print(a)

a = {}  #if we keep the content inside the curly braces as empty then it is a empty dictionary and not an empty set
print(type(a))  #will print that it is an empty dictionary

#an empty set can be created by using the below syntax:
a = set()
print(type(a)) #prints an empty set type

b = set()   #creating an empty set

#Adding values to set:

b.add(1)
b.add(55)
b.add(1)    #this is will not be added because it is a collection of non repetitive elements
b.add(1)    #adding a value repeatedly doesn't change a set
print(b)

#b.add([4,5,6])  #we can't add list to set because list is unhashable because list can be changed later

b.add((4,5,6))  #we can add a tuple to set because tuples are hashable that is they can be changed later
print(b)

#b.add({4:5})    #we can't add dictionary to set because dictionary is mutable too

print(len(b))   #Prints the length of this set
b.remove(1) #Removes 1 from set b
#b.remove(15)    #throws an error while trying to remove 15
print(b)

print(b.pop())  #removes the tuple since it is at top of stack
print(b)

