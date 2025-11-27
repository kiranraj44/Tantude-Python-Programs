import re 
d={}
pattern=r'[\d\-\s()]+'
x=input("Enter the text: ")
n=re.findall(pattern,x)
for i in n:
    clear=re.sub(r'\D','',i)
    if len(clear)==10:
        last4=clear[-4:]
        d[last4]=clear
print(d)