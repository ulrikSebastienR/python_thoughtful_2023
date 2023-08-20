#all extra trials such as without recursion and classes for the same function are at the end of this file

class IntegerOperations:
    "this class will contain operations on integers"
    def __init__(self, n=11, upper = 36):
        self.n = n
        self.upper = upper
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
    def atoi(self):
        "implement c style string of numbers to integer"
        pass
    def decimal_to_roman(self):
        "decimal to roman"
        pass
    def roman_to_decimal(self):
        "roman to decimal"
        pass
    def factors_without_repetition(self,number):#auot 20 INCOMPLETE
        factors = []
        for i in range(2,number+1):
            if number%i==0:
                factors.append(i)
                number == number//i
            if number==1:
                break
        return factors
    def factors_repetions_allowed(self,number): #auot 20 INCOMPLETE
        factors = []
        def f(number):
            for i in range(2,number+1):
                if number%i==0:
                    factors.append(i)
                    number==number//i
                    break
            if number==1:
                return factors
            else:
                return f(number)            
        #return factors
    def prime(self): #aout 13
        "check if n is prime or not"
        for i in range(2,self.n+1):
            if self.n%i == 0:
                break
        if i == self.n:
            return (self.n, "is a prime number")
        else:
            return i
    def prime_numbers_in_a_range(self):
        all_prime = []
        for number in range(2,self.upper+1):
            for i in range(2,number+1):
                if number%i==0:
                    break
            if i==number:
                all_prime.append(number)
        return all_prime 
    def prime_factorization(self, number):
        pass
io = IntegerOperations(11,360)

class FindCombinations:
    def __init__(self, n=27, l=[number for number in range(50)]):
        self.n = n
        self.l = l
    def make27_no_repetitions(self): #aout 13
        combs = []
        for first in self.l:
            for second in [number for number in self.l if number!=first]:
                if first+second == self.n:
                    this_comb = [first, second]
                    combs.append(this_comb)
        for item in combs:
            for item1 in [_ for _ in combs if _!=item]:
                if set(item)==set(item1):
                    combs.remove(item1)
        return combs                    
    def make27_repetitions_allowed(self):
        combs = []
        for item in self.l:
            for item1 in self.l:
                for item2 in self.l:
                    if item+item1+item2 == self.n:
                        combs.append([item,item1,item2])       
        return combs
    def indices_of_2_making_number(self,l=[number for number in range(50) if number%2!=0]):
        #leetcode problem no 1
        for i in range(len(l)):
            for j in range(len(l)):
                pass
        return i,j
    def sum_to_number_by3digits(self,current=[number for number in range(50) if number%2!=0], target=15):
        "comme 2+3+5=8 all unique triplets"
        return current#first, second, third
    def direct_closest_sum_duplicates_allowed(self,user_list=[number for number in range(50) if number%2!=0], target=51):
        "three numbers that when added get as close as possible to target where a number can appear more than once"
        to_compare,d = 2, {}
        for first in user_list:
            for second in user_list:
                for third in user_list:
                    diff = abs(target-first-second-third)
                    if diff<=to_compare:
                        to_compare=diff
                        output = [first, second, third] #this sum has duplicates
                        d.update({to_compare:output}) #to check the working
        return d#to_compare, output
    def closest_sum_using_dict_duplicates_allowed_working(self, target=51):
        "using dictionary three numbers that when added get as close as possible to target"
        d = {}
        for first in self.l:
            for second in self.l:
                for third in self.l:
                    diff = abs(target-first-second-third)
                    output = [first,second,third]
                d.update({diff:output})#play with placing d at the end of each loop
        for k, v in d.items():
            if k == min(d.keys()):
                first, second, third = d[k]
        return d#first,second,third
    def no_duplicates_sum_closest_to_target_working(self,user_list=[number for number in range(50) if number%2!=0], target=51):
        "allowing no duplicates closest sum to target"
        d,d1 = {},{}
        for first in user_list:
            for second in [number for number in user_list if number!=first]:
                for third in [number for number in user_list if number!=first and number!=second]:
                    diff = abs(target-(first+second+third))
                d.update({diff:[first,second,third]})#place d at end of each loop to see the inner working             
        for k in sorted(d.keys()):
            for key, value in d.items():
                if k == key:
                    d1.update({k:value})
        #for k in sorted(d.keys()):
        for key, value in d.items():
            if key == sorted(d.keys())[0]:
                closest = {key:value}
        return f"closest is {closest}, sorted dict is {d1} unsorted dict is {d} avec length {len(d)}"
    def no_duplicates_sum_closest_to_target_direct(self, user_list=[number for number in range(50) if number%2!=0],target=51):
        d,d1 = {},{}
        for first in user_list:
            for second in [_ for _ in user_list if _!=first]:
                for third in [_  for _ in user_list if _!= first and _!=second]:
                    diff = abs(target-first-second-third)
                    if diff <=3:
                        d.update({diff:[first,second,third]})
        return d[min(d.keys())]  #check return d as well pour la verification                      
    def bidirectional_search(self, target=51):
        return       
fc = FindCombinations()

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
d=d1={}


            
        



        
