import re
email_con='r^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
x=input("Enter the email id: ")
if re.search(email_con,x):
    print("True")
else:
    print("False")
