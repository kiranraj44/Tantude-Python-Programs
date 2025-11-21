def fac(n):
    if n<1:
        print("Not valid")
    else:
        fac=1
        for i in range(1,n+1):
            fac=fac*i
        return fac

x=int(input("Enter the factorial number: "))
print(fac(x))
