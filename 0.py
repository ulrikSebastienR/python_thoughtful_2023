#for a number in list do, find all combinations that make that number

def combinations_pour_a_list(user_list = [number for number in range(10)]):
    d = {}
    for number in user_list:
        digi = [_ for _ in range(int(number/2+1))]
        insidel = [[char] for char in "abcdefgh"]
        for i in range(len(digi)):
                       insidel[i].append(digi[i])
                       insidel[i].append(number-digi[i])
        for sublist in insidel:
            sublist.pop(0)
        final = [x for x in insidel if x]
        d.update({number:final})
    return d

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

    def removal_from_r_wrong1(self): #should never be attempted deletion of elements from list under current iteration
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
x = Make7()
y = Make7(9,[1]) #values surpassing the default values for positional arguments
#z = Make7({l:[2], n:8}) doesnt work      

class RemoveEmptySublists:
    "empty lists are false objects so cant be removed by l.remove"
    def __init__(self, l=[[char] for char in "abcdefghi"], digits= [number for number in range(int(7/2+1))]):
        self.l = l
        self.digits = digits  #from make7 or combinations making a number program
        for i in range(len(self.digits)): #you can run a code in class definiton if a code is common to the class
            self.l[i].append(self.digits[i])#note this and next line since this is class definition so self.l and l are interchangable
            l[i].append(7-self.digits[i]) #note this and previous line
        for sublist in self.l:
            sublist.pop(0)      

    def correct_method(self):
        self.l = [sublist for sublist in self.l if sublist !=0]
        return self.l #[[0, 7], [1, 6], [2, 5], [3, 4]]
    
    def correct2(self):
        self.l = [sublist for sublist in self.l if sublist]
        return self.l #[[0, 7], [1, 6], [2, 5], [3, 4]]
    
    def wrong_method(self):
        for sublist in self.l:
            if sublist == []:
                self.l.remove(sublist)
        return self.l #[[0, 7], [1, 6], [2, 5], [3, 4], [], []]

    def wrong2(self):
        for i in range(len(self.digits)): #we need it here separately but need to comment out same code in class definition otherwise same code would run twice
            self.l[i].append(self.digits[i])
            self.l[i].append(7-self.digits[i])
##        for sublist in self.l:
##            sublist.pop(0)
##            if sublist == []:
##                self.l.remove(sublist)             
        return self.l
z = RemoveEmptySublists()    
    



"""for 0 combinations are [['a', 0, 0], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h']]
for 1 combinations are [['a', 0, 0, 0, 1], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h']]
for 2 combinations are [['a', 0, 0, 0, 1, 0, 2], ['b', 1, 1], ['c'], ['d'], ['e'], ['f'], ['g'], ['h']]
for 3 combinations are [['a', 0, 0, 0, 1, 0, 2, 0, 3], ['b', 1, 1, 1, 2], ['c'], ['d'], ['e'], ['f'], ['g'], ['h']]
for 4 combinations are [['a', 0, 0, 0, 1, 0, 2, 0, 3, 0, 4], ['b', 1, 1, 1, 2, 1, 3], ['c', 2, 2], ['d'], ['e'], ['f'], ['g'], ['h']]
{0: [['a', 0, 0, 0, 1, 0, 2, 0, 3, 0, 4], ['b', 1, 1, 1, 2, 1, 3], ['c', 2, 2], ['d'], ['e'], ['f'], ['g'], ['h']], 1: [['a', 0, 0, 0, 1, 0, 2, 0, 3, 0, 4], ['b', 1, 1, 1, 2, 1, 3], ['c', 2, 2], ['d'], ['e'], ['f'], ['g'], ['h']], 2: [['a', 0, 0, 0, 1, 0, 2, 0, 3, 0, 4], ['b', 1, 1, 1, 2, 1, 3], ['c', 2, 2], ['d'], ['e'], ['f'], ['g'], ['h']], 3: [['a', 0, 0, 0, 1, 0, 2, 0, 3, 0, 4], ['b', 1, 1, 1, 2, 1, 3], ['c', 2, 2], ['d'], ['e'], ['f'], ['g'], ['h']], 4: [['a', 0, 0, 0, 1, 0, 2, 0, 3, 0, 4], ['b', 1, 1, 1, 2, 1, 3], ['c', 2, 2], ['d'], ['e'], ['f'], ['g'], ['h']]}"""



#intended output was to find combinations that can make 5 [[1,4],[2,3]]
#coudnt do with sublist nested for loops
#l = [[].append(char) for char in "abcde"] #wont work
n = 5
l = [[]]*int(n/2) #improper output because lists initialized this way all point to same object
p = [[char] for char in "abcde"]
q = [[0]]*int(n/2) #problem is they all point to the same object
t = [[9]]*int(n/2) #lists initialized this way all point to same object and hence no proper output
r = [_ for _ in range(1,int(n/2+1))]
s = [char for char in "abcde"]


d = dict(zip(r,s))
#append to dict 
d.update({"aa":1000})

for i in range(int(n/2)):
    p[i].append(r[i])
    p[i].append(n-r[i]) #output p = [['a', 1, 4], ['b', 2, 3], ['c'], ['d'], ['e']]
    q[i].append(r[i])
    q[i].append(n-r[i]) #output q =  [[0, 1, 4, 2, 3], [0, 1, 4, 2, 3]]   
    l[i].append(r[i])
    l[i].append(n-r[i]) #output l = [[1, 4, 2, 3], [1, 4, 2, 3]]
    t[i].append(r[i])
    t[i].append(n-r[i]) # [[9, 1, 4, 2, 3], [9, 1, 4, 2, 3]]



    
    


l = [[]]*6
n = 5
r = [number for number in range(int(n/2)+1)]

for number in r:
     for sublist in l:
          sublist.append(number)
          sublist.append(n-number)
          r.remove(number)
          
          

##for sublist in l:
##     for number in r:
##         sublist.append(number)
##         sublist.append(n-number)
##         break
##     r.remove(number)
##     #break gives output [[0, 5], [0, 5], [0, 5], [0, 5], [0, 5], [0, 5]]
##     #continue or without continue gives [[0, 5, 1, 4, 2, 3], [0, 5, 1, 4, 2, 3], [0, 5, 1, 4, 2, 3], [0, 5, 1, 4, 2, 3], [0, 5, 1, 4, 2, 3], [0, 5, 1, 4, 2, 3]]
##


     
def make_5(n):
    "finds all combinations that when added make number 5 or n"
    l = [[]]*n
    
    for sublist in l:
        to_browse = [_ for _ in range(1,int(n/2)+1)]
        for number in to_browse:
            sublist.append(number)
            sublist.append(n-number)
            
            break
        to_browse.remove(number) #should never be deleted from the list under iteration
        #break
        
    return to_browse, l
        
            
            
