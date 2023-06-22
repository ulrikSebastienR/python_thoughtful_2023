#using swap, incomplete yet
x, y = 0,1
def fibb(x,y):
    x, y = y, x+y
    return x,y

l1 = [0]
for i in range(19):
    #print(x,y)
    x,y = fibb(x,y)
    #print(x,y)
    l1.append(y)

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


