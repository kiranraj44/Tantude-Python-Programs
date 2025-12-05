from math import gcd
from functools import reduce

def lcm(m,n):
    return m*n//gcd(m,n)

count=0

a=list(map(int,input("Enter the 1st array: ").split()))
b=list(map(int,input("Enter the 2nd array: ").split()))
x=reduce(lcm,a)
y=reduce(gcd,b)

for i in range(x,y+1):
    c1=all([i%num_a==0 for num_a in a])
    c2=all([num_b%i==0 for num_b in b])
    count+=c1*c2

print(count)
