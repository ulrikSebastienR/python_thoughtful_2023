#using swap
x, y, l = 0,1, [0]
def fib(x,y):
    x, y = y, x+y
    return x,y

for i in range(n-1):
    x, y = fib(x,y)
    l.append(y)

#using recursion without swap
def fib(n):
    if n<0:
        return 0
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
l = []
for i in range(19):
    l.append(fib(i))


