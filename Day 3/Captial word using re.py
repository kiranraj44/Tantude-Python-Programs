import re
cap_word=r'\b[A-Z][a-zA-Z]*'
x=input("Enter the List: ")
n=re.findall(cap_word,x)
print(n)

