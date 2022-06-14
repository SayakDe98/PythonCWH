
#Lists are mutable

#Create a list using []
a = [1, 2 , 3 , 4 , 56 , 6]

#Print the list using print() function
print(a)

#Access using index a[0], a[1], a[2]
print(a[0])

#value is getting changed since lists are mutable
a[0] = 98   
print(a[0])

#we can create a list with items of different types
c = [45 , "Harry" , False , 6.9]    #this is valid
print(c)

#List slicing
friends = ["Harry" , "Tom" , "Rohan" , "Sam" , "Divya" , 45]
print(friends[0 : 4])
print(friends[-4:])

