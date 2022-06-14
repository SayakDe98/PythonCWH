# n! = 1X2X3X4X5X6X7X8X9...Xn
# 5! = 1X2X3X4X5

num = int(input("Enter the number : "))

factorial=1
for i in range(1,num+1):
    factorial*=i
print(f"The factorial of {num} is {factorial}")
