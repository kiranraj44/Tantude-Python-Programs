import re
d={}
pattern=r'\s*Student:\s*(\w+)\s*Subject:\s*(\w+)\s*Score:\s*(\d+)'
x=input("Enter the text: ")
n=re.findall(pattern,x)
for name,sub,score in n:
    score=int(score)
    if name not in d:
        d[name]={}
    d[name][sub]=score
print(d)    