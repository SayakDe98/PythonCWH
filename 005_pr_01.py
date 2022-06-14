def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:#i.e. num3>num1
        if(num3>num2):
            return num3
        else:
            return num2
m=maximum(13,5,222)
print('The maximum value is : '+str(m))