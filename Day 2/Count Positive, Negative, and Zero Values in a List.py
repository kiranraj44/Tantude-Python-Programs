list1=list(map(int,input("Enter numbers separated by space: ").split()))
print("List:", list1)
positive_count=0
negative_count=0
zero_count=0
for i in list1:
    if i<0:
        negative_count+=1
    elif(i>0):
        positive_count+=1
    else:
        zero_count+=1
print("positive= ",positive_count)    
print("negative= ",negative_count)
print("zero= ",zero_count)
