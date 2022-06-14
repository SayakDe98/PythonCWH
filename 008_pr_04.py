#n!-(n-1)!*n
#sum(n)=sum(n-1)+n
def recursive_sum(n):
    if n==0:return 0
    else:
        return recursive_sum(n-1)+n

s=recursive_sum(10)
print(s)