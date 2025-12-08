l1=list(map(int,input("Enter the number: ").split()))
n=len(l1)
count=0
k=int(input("Enter the digit to get divised by: "))
for i in range(n):
    for j in range (i+1,n):
        if (l1[i]+l1[j])%k==0:
            count+=1
print("Count: ",count)
