greeting = "Good Morning, "
name = "Sayak"
print(name[4])
# print(type(name))

#Concatenate two strings
print(greeting + name)

#strings are immutable

#slicing 
print(name[0:3])

#if we are given a string and we don't know the length we can make
#use of negative index, we can use -1 index to get last index
print(name[:4]) # is same as name[0:4]
print(name[0:]) # is same as name[0:last index]
# for "sayak" k's negative index is -1,...,s's last index is -5
c = name[-4 : -1] # is same as name[1 : 4]
print(c)

#Slicing with skip value
d = name[1 : 4 : 2] # since there is 2 hence there will be a skip of 1 element
print(d)
d = name[0::2] #we left end index hence we go till last
print(d)

