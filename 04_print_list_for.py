fruits = ["Banana" , "Watermelon" , "Grapes" , "Mango"]

for item in fruits:
    print(item)

print("Using range() function : ")
for item in range(0,len(fruits)):
    print(fruits[item])

print("All fruits from 2 to end")
for item in range(2,len(fruits)):
    print(fruits[item])

print("Print all numbers from 1 to 8:")
for i in range(1,8):    #equivalent of this is for i in range(1,8,1)
    print(i)

print("Print alternate numbers:")
for i in range(0,8,2):
    print(i)