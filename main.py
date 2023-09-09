# implement a recursive function to calculate the factorial of a given number 
def factorial(x):
  if x==1:
    return 1
  else:
    return x*factorial(x-1)
f=factorial(4)
print("factorial of 4 is",f)
