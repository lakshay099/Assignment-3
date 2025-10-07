def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

x=int(input("Enter a positive integer:"))
print("factorial of",x,"is", factorial(x))