#write your function thinking what you want it to do

class UsingRecursion:
    "in recursion return function itself except for terminating condition for the function where it would return the output variable" 
    def __init__(self, number=6):
        self.number = number
    def fibb_recursion(self):
        def inner_fibb(i): #nested functions
            if i<=0:
                return 0
            elif i==1:
                return 1
            else:
                return inner_fibb(i-2)+inner_fibb(i-1)
        l = []
        for i in range(self.number):
            l.append(inner_fibb(i))
        return l
    def factorial(self,n):
        if n<=1:
            return 1
        else:
            return self.factorial(n-1)*n
    def power(self, raised):
        if raised <=1:
            return self.number
        else:
            return self.number*self.power(raised-1)
ur = UsingRecursion()

class WithoutRecursion:
    def __init__(self, number=6):
        self.number = number
    def factorial(self):
        fact = 1
        for i in range(1,self.number+1):
            fact = i*fact
        return fact            
    def fibb(self):
        x,y,l = 0,1,[0] #do later solution underneath
        def innerfibb(x,y):
            y,x = x+y, y
            return x,y
        for i in range(self.number-1):
            x,y = innerfibb(x,y)
            l.append(x)
        return l
wr = WithoutRecursion()

class WhileExamples:
    def __init__(self, number=5):
        self.number = number
    def factorial_while(self):
        fact,i = 1,1 #cant do fact=i=1, doing so will make both point to the same object
        while i!=self.number+1:
            fact = i*fact
            i+=1
        return fact            
we = WhileExamples()

class ForExamples:
    def __init__(self, number=5):
        self.number = number
    def factorial_for(self):
        fact = 1
        for i in range(1,self.number+1):
            fact = fact*i
        return fact
    def fibb(self):
        x,y, l = 0,1, [0]
        def inner_fibb(x,y): #une example de inner function
            y,x = x+y, y
            return x,y
        for i in range(self.number-1):
            x, y = inner_fibb(x,y) #this is not concurrent modification because you are not modifying the object under iteration
            l.append(y)
        return l        
fe = ForExamples()



##
###fibbonaci with recursion 
##def fib(n):
##    if n<0:
##        return 0
##    elif n==0:
##        return 0
##    elif n==1:
##        return 1
##    else:
##        return fib(n-1)+fib(n-2)
##l = []
##for i in range(19):
##    l.append(fib(i))
###fibbonaci without recursion using for
##x, y, fibbl, n = 0,1, [0,1], 5
##def fibb(x,y):
##    x, y = y, x+y
##    return x,y
##for i in range(0,n-2):
##    x, y = fibb(x,y)
##    fibbl.append(y)
##
###fibbonaci without recursion using while 
##i, x, y, fibbw = 0,0,1, [0,1] #to provide iterator value to while to stop running it infinitely
##def fibb_w(x,y):
##    x, y = y, x+y
##    return x,y
##while i != n-2:
##    x, y = fibb_w(x,y)
##    i+=1
##    fibbw.append(y)
##
###factorial without recursion
##n, product = 3, 1
####def f(n): can use this function as well
####    return n
##for i in range(n,0,-1):
##    product = i*product   
###factorial with recursion
##def factorial(n):
##    if n<0:
##        return 1
##    elif n==0:
##        return 1
##    elif n==1:
##        return 1
##    else:
##        return n*factorial(n-1)
##    
###prime factorization
### first find possible prime numbers using flag prime number in a range, doesnt include 2 
##n, prime_numbers = 2356, [2]
##for number in range(2, n):
##    flag = False
##    for i in range(2,number):
##        if number%i == 0:
##            break
##        else:
##            flag = True
##        if i == number-1: #this is done to ensure loop runs to the end otherwise loop will output prime number first time remainder isnt zero
##            prime_numbers.append(number)
###prime factorization using recursion 
##pf = []
##def factors(n):
##    if n ==1:
##        return pf
##    else:
##        for i in prime_numbers:
##            if n%i == 0:
##                pf.append(i)
##                quotient = n//i
##                return factors(quotient)
##n = 16
##x = factors(16)
##l = [str(i) for i in pf]
##print(n, "=", "*".join(l))
##
###prime factorization without recursion
##pf = [] #we are referring as quotient the number whose prime factors we are supposed to find like 6 or 15 or 120 etc
##def factors(quotient):
##    while quotient !=1:
##        for number in prime_numbers:
##            if quotient%number ==0:
##                break
##        pf.append(number)
##        quotient = quotient//number
##    return pf
##x = factors(6) #print(pf)
##    
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##

##pfwr, n = [], 21
##def factorswr(n):
##    for number in prime_numbers:
##        if n%number ==0:
##            pfwr.append(number)
##            quotientwr = n//number
##    return quotientwr, pfwr
##
##quotientwr, pfwr = factorswr(n)
##
##if quotientwr!=1:
##    factorswr(quotientwr)


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = i*fact
    return fact
       
       

