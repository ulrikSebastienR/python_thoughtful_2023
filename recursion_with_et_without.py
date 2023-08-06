#write your function thinking what you want it to do
#in recursion return function itself except for terminating condition for the function where it would return the output variable 

class UsingRecursion:
    def __init__(self, n=6):
        self.n = n
    def fibb(self):
        if self.n <=1:
            return 0
        elif self.n==2:
            return 1
        else:
            return self.fibb(self.n-1)+self.fibb(self.n-2)        
ur = UsingRecursion()

class WithoutRecursion:
    def __init__(self, n=6):
        self.n = n
    def fibb(self):
        pass
wr = WithoutRecursion()

class WhileExamples:
    def __init__(self, n=5):
        self.n = n
we = WhileExamples()

class ForExamples:
    def __init__(self, n=5):
        self.n = n
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

