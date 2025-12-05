a=list(map(int,input("Enter the scores: ").split()))
l=[]
for i in a:
    if(i<=38):
        l.append(i)
    else:
        d=((i//5)+1)*5
        if(d-i)<3:
            l.append(d)
        else:
            l.append(i)
print(l)
        
