l1=list(map(int, input("Enter the list: ").split()))
d=int(input("Enter d: "))
m=int(input("Enter m: "))
count = 0
for i in range(len(l1)-m+1):
    if sum(l1[i:i+m])==d:
        count += 1
print(count)

        
   
