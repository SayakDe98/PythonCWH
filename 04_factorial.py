#n!=1*2*3*4*...*n
#n!=[1*2*3*4...(n-1)]*n
#n!=(n-1)!*n

print("Without using function:")
n=4
product=1
for i in range(n):
    product=product*(i+1)
print(product)

print("With using function:")
def factorial_iter(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product
print(factorial_iter(4))

print("With using recursion:")
def factorial_recursive(n):
    if(n==0):return 1
    return n*factorial_recursive(n-1)
f=factorial_recursive(4)
print(f)
