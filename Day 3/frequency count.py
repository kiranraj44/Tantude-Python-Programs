n=input("Enter the name: ")
d={}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
