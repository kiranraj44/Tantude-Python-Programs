n=int(input("Enter the number: "))
l=len(str(n))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**l
    temp=temp//10
    
if sum==n:
    print("Its a Amstrong number")
else:
    print("Its not a Amstrong number")
