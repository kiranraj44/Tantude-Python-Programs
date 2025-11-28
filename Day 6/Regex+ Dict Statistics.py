import re
d={}
pattern=r'(\w+):\s*(⭐+)'
x=input("Enter the text: ")
n=re.findall(pattern,x)
for product,stars in n:
    star_count=len(stars)
    if product not in d:
        d[product]=[]
    d[product].append(star_count)
    
avg={product:sum(vals)/len(vals) for product,vals in d.items()}
print(avg)