#WAP to find the sum of first n natural numbers using while loop
from re import I


n = int(input('Enter a number upto which we need sum:'))
sum = 0
i=1 
while(i<=n):
    sum+=i
    print(f"Sum is = {sum}")
    i+=1