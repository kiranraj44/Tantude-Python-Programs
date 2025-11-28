import re 
d={}
pattern=r'\[(.*?)\]\s*Module:\s*(\w+)\s*Time:\s*([\d.]+)'
x=input("Ente the text: ")
n=re.findall(pattern,x)
print(n)
for date,module,time in n:
    time_val=float(time)
    if date not in d:
        d[date]={}
    if module not in d[date]:
        d[date][module]=[]
    d[date][module].append(time_val)    
    
avg={date:{module:sum(times)/len(times) for module,times in mods.items()} for date,mods in d.items()}
print(avg) 