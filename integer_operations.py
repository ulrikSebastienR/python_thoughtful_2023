#all extra trials such as without recursion and classes for the same function are at the end of this file
def exponent(number, power):
    "calculates value of a number when raised by an exponent"
    product = 1
    for _ in range(power):
        product = number*product
    return product

def greatest(l):
    " finds greatest of given number"
    greatest = l[0]
    for item in l:
        if item > greatest:
            greatest = item
    return greatest
        

def factorial(n):
    if n <= 0:
        return 0
    elif n==1:
        return 1
    else:
        return factorial(n-1)*n

def permutations(n,r):
    ''' total number of arrangements in selection'''
    perm = factorial(n)/factorial(n-r)
    return perm

def combinations(n,r):
    '''ways to select r items from total n items'''
    comb = factorial(n)/factorial(n-r)/factorial(r)
    return comb

#without recursion/for/while/ method other than previously used in this file

def factorial_while(n):
    "factorial using while loop"
    factw = 1
    while n!=1:
        factw =  n*factw
        n -= 1
    return factw

def factorial_for(n):
    ''' factorial using for loop without recursion'''
    factf = 1
    for i in range(n,1,-1):
        factf = i*factf
    return factf

x, y, l, n = 0,1, [0,1], 0
def fibb_while(x, y, n):
    x, y = y, x+y
    return x, y

while n!= 6-2:
    x, y = fibb_while(x,y,n)
    n+=1
    l.append(y)

    

#classes for functions already wrote

factw = 1
class IntegerOperations:
    "this class will contain operations on integers"
    def __init__(self, n):
        self.n = n
        
    def factorial_while(self):
        global factw #use of global variable to use a variable declared outside the class
        while self.n!=1:
            factw = self.n*factw
            self.n-=1
        return factw

    def factorial_for(self):
        factf = 1 #declare inside to avoid local variable referenced before assignment
        for i in range(self.n, 1, -1):
            factf = factf*i
        return factf

trial = IntegerOperations(6)
        
