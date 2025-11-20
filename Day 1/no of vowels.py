x=input("Enter the word: ")
a=x.lower()
print(a)
count=0
list1=["a","e","i","o","u"]
for i in a:
    if i in list1:
        count=count+1
print("no of vowels: ",count)    
