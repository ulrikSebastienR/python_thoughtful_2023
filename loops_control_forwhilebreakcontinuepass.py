#continue takes control back to first line of the loop, break terminates any loop and pass does nothing
#you can update item to traverse (like a list) in the loop itself and loop will traverse the updated list from next iteration
#while loop can not update itself and you need to provide value of iterator for the next step otherwise it will keep on hanging on the very first iteration

class Make7:
   # n = 7 class variable
    "find all numbers that when added make 7" 
    def __init__(self,n=7,l=[[char] for char in "abcde"]): #no need to pass any instance variables if you have initialized them in class definition, these are positional arguments with default values
        self.n = n
        self.l = l
        self.r = [number for number in range(int(self.n/2+1))]

    def instance_variables(self):
        return self.l, self.n, self.r

    def correct(self):
        "correct method to get the desired output"
        for i in range(len(self.r)):
            self.l[i].append(self.r[i])
            self.l[i].append(self.n-self.r[i])
            self.l[i].pop(0)
        return self.l #[[0, 7], [1, 6], [2, 5], [3, 4], ['e']]               

    #now come the experiments to learn break and continue
    def wrong1(self):
        "experiments to learn break and loop control without removing numbers from r"
        for number in self.r:
            for sublist in self.l:
                sublist.append(number)
                sublist.append(self.n-number) 
                #break [[0, 7, 1, 6, 2, 5, 3, 4], [], [], [], []]
            #break [[0, 7], [0, 7], [0, 7], [0, 7], [0, 7]] 
        for sublist in self.l:
            sublist.pop(0)
        return self.l #[[0, 7, 1, 6, 2, 5, 3, 4], [0, 7, 1, 6, 2, 5, 3, 4], [0, 7, 1, 6, 2, 5, 3, 4], [0, 7, 1, 6, 2, 5, 3, 4], [0, 7, 1, 6, 2, 5, 3, 4]]

    def removal_from_r_wrong1(self):
        "removing numbers from r after loop runs"
        print(self.r)
        for number in self.r:
            print(f"number is {number}")
            for sublist in self.l:
                try:
                    sublist.append(number)
                    sublist.append(self.n-number)
                    print(f"l is {self.l}")
                    print(f"number after sublist loop is {number}")
                    #self.r.remove(number) [[0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5]]
                    #print(f"r is {self.r}")
                except:
                    pass
            print(f"number after sublist loop is {number}") #CANT UNDERSTAND WHY LOOP NEVER GOES TO 1 AND 3
            self.r.remove(number) #[[0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5]]
        for sublist in self.l:
            sublist.pop(0)
        return self.l
                
    def failed2(self):
        "putting sublist first"
        print(self.r)
        for sublist in self.l:
            for number in self.r:
                sublist.append(number)
                sublist.append(self.n-number)
                #break [[0, 7], [0, 7], [0, 7], [0, 7], [0, 7]]
            break
            sublist.pop(0)#note in earlier functions we need to run a loop to pop from sublists as we were putting numbers first in above functions
        return self.l #[[0, 7, 1, 6, 2, 5, 3, 4], [0, 7, 1, 6, 2, 5, 3, 4], [0, 7, 1, 6, 2, 5, 3, 4], [0, 7, 1, 6, 2, 5, 3, 4], [0, 7, 1, 6, 2, 5, 3, 4]]

    def sublist_first_failed(self):
        for sublist in self.l:
            for number in self.r:
                sublist.append(number)
                sublist.append(self.n-number)
                #break [[0, 7], [0, 7], [0, 7], [0, 7], [0, 7]]
                #self.r.remove(number)
            #break [['a', 0, 7, 1, 6, 2, 5, 3, 4], ['b'], ['c'], ['d'], ['e']]
            sublist.pop(0)
            #break [[7, 1, 6, 2, 5, 3, 4, 0, 7, 1, 6, 2, 5, 3, 4], ['b'], ['c'], ['d'], ['e']]
        return self.l

    def sublist_first_removal_from_r(self):
        pass
  
x = Make7()
y = Make7(9,[1]) #values surpassing the default values for positional arguments
#z = Make7({l:[2], n:8}) doesnt work

def make7_1():
    l, n = [[char] for char in "abcde"], 7
    r = [number for number in range(1, int(n/2+1))]
    "find all numbers that when added make 7, no repetitions, learn break and continue in process"
    for number in r:
        for sublist in l:
            sublist.append(number)
            sublist.append(n-number)
            #sublist.pop(0) #output with pop here [[2, 5, 3, 4], [2, 5, 3, 4], [2, 5, 3, 4], [2, 5, 3, 4], [2, 5, 3, 4]]
        #sublist.pop(0) [['a', 1, 6, 2, 5, 3, 4], ['b', 1, 6, 2, 5, 3, 4], ['c', 1, 6, 2, 5, 3, 4], ['d', 1, 6, 2, 5, 3, 4], [2, 5, 3, 4]]
    return l #[['a', 1, 6, 2, 5, 3, 4], ['b', 1, 6, 2, 5, 3, 4], ['c', 1, 6, 2, 5, 3, 4], ['d', 1, 6, 2, 5, 3, 4], ['e', 1, 6, 2, 5, 3, 4]]

def make7_2():
        l, n = [[char] for char in "abcde"], 7
        r = [number for number in range(1, int(n/2+1))]
        "trying to remove character in sublists"
        for number in r:
            for sublist in l:
                #sublist.pop(0) #cant do pop as item at index 0 will change with every run of the loop
                sublist.append(number)
                sublist.append(n-number)
                #sublist.remove("a")
                #break #[['a', 1, 6, 2, 5, 3, 4], ['b'], ['c'], ['d'], ['e']]
            break #[['a', 1, 6], ['b', 1, 6], ['c', 1, 6], ['d', 1, 6], ['e', 1, 6]]
        return l
    
def make7_3():
    l, n = [[char] for char in "abcde"], 7
    r = [number for number in range(1, int(n/2+1))]
    "find all numbers that when added make 7, no repetitions, learn break and continue in process"
    try:
        for number in r:
            for sublist in l:
                sublist.append(number)
                sublist.append(n-number)       
                r.remove(number)
    except:
        pass
    return l


l, k = [number for number in range(6,66,6)], []

def sqroot_while(n):
    "using while to calculate sq root"
    number = 0
    while number<int(n/2)+1:
        if n == number*number:
            return number
            break
        else:
            number+=1

def sqroot_for(n):
    "using for to calculate square root"
    for number in range(int(n/2+1)):
        if n == number*number:
            return number
            break    
for item in l:
    k.append(sqroot_while(item)) #returns none for number with float square roots

#simplest
for i,item in enumerate(l):
    if item%4==0:
        print(item)
print("----")

#using while 
for i in l:
    #print("-")
    while i %4==0:
        print(i)
        i += 6
print("------")    

# a better way to do above
for i in range(len(l)):
    #print(i,l[i])
    while l[i]%4 ==0:
        print(l[i])
        i += 1
        if i == len(l):
            break
print("-----")

#continue throws control back to start of the loop ignoring all remaining statements
for i,item in enumerate(l):
    if item%4==0:
        print(item)
        continue
        print(i,item)
print("----- DOING VIA ENUMERATE AND WHILE")

#doing via enumerate and while
for i,item in enumerate(l):
    while item%4 ==0:
        print(item)
        i+=1
        break

print("SOME EXAMPLES ON WHILE")

print("SORT A LIST USING WHILE")
l1 = [31, 23, 83, 12, 86, 97, 34, 18]
l_s = []
while len(l1)!=0:
    l_s.append(min(l1))
    l1.remove(min(l1))
print(l_s)

#if a number is prime using while loop
n = 13
i = 2
while i!=n-1:
    if n%i ==0:
        break
    i +=1
    if i == n-1:
        print(f"{n} is a prime number")

#if a number is prime using for loop
for i in range(2,n):
    if n%i ==0:
        break
    else:
        pass
    if i == n-1:
        print(f"{n} is a prime number by for loop")        

def example1():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    l = [[char] for char in "ab"]
    for number in [1,2]:
        for sublist in l:
            sublist.append(number)
            print(l)
    return l #output [['a', 1, 2], ['b', 1, 2]]

def example2():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    l = [[char] for char in "ab"]
    for number in [1,2]:
        for sublist in l:
            sublist.append(number)
            print(l)
            break
    return l #output [['a', 1,2], ['b']]

def example3():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    l = [[char] for char in "ab"]
    for number in [1,2]:
        for sublist in l:
            sublist.append(number)
            print(l)
            break
        break
    return l #output [['a',1], ['b']]

def example4():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    l = [[char] for char in "ab"]
    for number in [1,2]:
        for sublist in l:
            sublist.append(number)
            print(l)
            break
    #break
    return l #output break outside loop error

def illustration1():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    l = [[char] for char in "ab"]
    for sublist in l:
        for number in [1,2]:
            sublist.append(number)
            print(l)
    return l #output [['a', 1, 2], ['b', 1, 2]]

def make5_1():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    n = 5
    l = [[char] for char in "abcde"]
    r = [number for number in range(1,int(n/2+1))]
    try:
        for number in r:
            print(r)
            for sublist in l:
                print(r)
                print(number)
                sublist.append(number)
                sublist.append(n-number)
                print(l)
                r.remove(number)
                print(f"r is {r}")
                print(l)
        #return l #[['a', 1, 4], ['b', 1, 4], ['c'], ['d'], ['e']]
    except: #to bypass the error x not in list as list finally has no elements
        pass
    return l


        



        

