import re
d={}
pattern=r'[A-Z]+[a-z]+'
x=input("Enter the text: ")
n=re.findall(pattern,x)
for i in n:
    d[i]=d.get(i,0)+1
print(d)


