import re
d={}
pattern=r'\[(.*?)\]\s*User:\s*(\w+)\s*Action:\s*(\w+)'
x=input("Enter the text: ")
n=re.findall(pattern,x)
for date,user,action in n:
    if user not in d:
         d[user]={}
    d[user][date]=action
print(d)