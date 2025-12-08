import re 
d={}
pattern=r'\s+(\w+):\s+([^[]+)\s'
x=input("Enter the text: ")
n=re.findall(pattern,x)
for user,msg in n:
    if user not in d:
        d[user]=[]
    d[user].append(msg)
print(d)
