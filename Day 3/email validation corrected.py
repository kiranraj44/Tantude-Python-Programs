import re
email_con=r'^[a-zA-Z]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,}$'
x=input("Enter the email id: ")
if re.search(email_con,x):
    print("True")
else:
    print("False")
