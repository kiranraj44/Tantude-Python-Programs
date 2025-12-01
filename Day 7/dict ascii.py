import re 
d={}
pattern=r'.'
x=input("Enter the text: ")
n=re.findall(pattern,x)
a={i:ord(i)for i in n}
print(a)