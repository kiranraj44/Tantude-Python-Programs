import re
d={}
pattern=r'([A-Za-z]+)\((PERSON|ORG|LOC)\)'
x=input("Enter the text: ")
n=re.findall(pattern,x)
for name,tag in n:
    if tag not in d:
        d[tag]=[]
    d[tag].append(name)
print(d)    
