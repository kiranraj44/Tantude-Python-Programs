def sum(n):
  if n == 1:
    return 1
  return n + sum(n-1)

x=int(input("Enter the n numbers: "))
print(sum(x))
