x, y,n, l = 0,1, 5, [0,1]
def fibb(x,y, n): #why my function not throwing local 
    x, y = y, x+y
    return x,y

for i in range(n-2):
    x,y = fibb(x,y, i)
    l.append(y)
