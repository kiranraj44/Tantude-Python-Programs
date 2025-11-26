import re
def extract_emails(text):
    pattern=r'[a-zA-Z]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,}'
    n=re.findall(pattern,text)
    return{email:email.split('@')[1] for email in n}
a=input("Enter the text: ")
print(extract_emails(a))

  
