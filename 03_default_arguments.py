def greet(name="Stranger"):#default argument "Stranger" is provided
    print("Good Day, "+name)

greet("Sayak")

def mySum(num1,num2):
    return num1+num2

s=mySum(6,32)
print(s)

greet()#we have default argument so even if we don't pass any argument
#then only there is no problem