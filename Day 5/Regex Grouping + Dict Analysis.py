import re
d={}
x=input("Enter the text: ")
pattern=r'([A-ZAa-z]+):\s*(\d+)'
n=re.findall(pattern,x)
for name,mark in n:
    mark=int(mark)
    if name not in d:
        d[name]=[]
    d[name].append(mark)
avg={name:sum(mark)/len(mark) for name,mark in d.items()}
print(avg)