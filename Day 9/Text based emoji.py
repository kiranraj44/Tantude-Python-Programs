import re
x=input("Enter the text: ")
pattern=r'[(:)]|[:(]|[<3])'
n=re.findall(pattern,x)
d={}
for i in n:
    if i==":)":
        d[i]="smile"
    elif i==":(":
        d[i]="sad"
    elif i=="<3":
        d[i]="love"
print(d)