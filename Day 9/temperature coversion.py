l1=list(map(int,input("Enter the digits: ").split()))
d={}
for i in l1:
    f = (i * 9/5) + 32
    d[i]=round(f,1)
print(d)