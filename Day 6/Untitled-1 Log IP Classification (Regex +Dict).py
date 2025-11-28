import re
pattern=r'\s*([\d\.]+)'
x=input("Enter the text: ")
n=re.findall(pattern,x)
result={'private':[],'public':[]}
for ips in n:
    a,b,c,d=map(int,ips.split('.'))
    if(a == 10 or(a == 172 and 16 <= b <= 31)or(a == 192 and b == 168)):
        result['private'].append(ips)
    else:
        result['public'].append(ips)
print(result)
