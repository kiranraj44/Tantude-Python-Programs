x=input("Enter the word for palindrome check: ")
s=x[::-1]
if x in s:
    print("Yes")
else:
    print("No")
