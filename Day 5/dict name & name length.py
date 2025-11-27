import re
d={}

pattern=r'[A-Za-z]+'
x=input("Enter the text: ")
n=re.findall(pattern,x)
for i in n:
    d[i]=len(i)       
print(d)
