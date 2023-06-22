n = 14
i = 2
while i!=n-1:
    if n%i ==0:
        break
    i +=1
    if i == n-1:
        print(f"{n} is a prime number")

for i in range(2,n-1):
    if n%i ==0:
        break
    else:
        pass
    if i == n-1:
        print(n)

x, y, l = 0,1, [0]
def fib(x,y):
    x, y = y, x+y
    return x,y

for i in range(n-1):
    x, y = fib(x,y)
    l.append(y)
