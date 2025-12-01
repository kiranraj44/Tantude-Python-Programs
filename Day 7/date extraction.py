import re 
d={}
pattern=r'\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b|\b\d{2}-[A-Za-z]{3}-\d{4}\b'
x=input("Enter the text: ")
n=re.findall(pattern,x)
for date,count in enumerate(n):
    d[date]=count
print(d)