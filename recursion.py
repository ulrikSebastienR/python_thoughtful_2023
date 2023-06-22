#fibbonaci
def fib(n):
    if n<0:
        return 0
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
l = []
for i in range(19):
    l.append(fib(i))

#factorial
def factorial(n):
    if n<0:
        return 1
    elif n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
    
