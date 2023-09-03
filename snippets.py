#do combinations by removing duplicates from permutations#longest closing parentheses#merge intervals#group patterns in a number such as 123456123456123456123456123456
# an empty hash means starting of a new snippet
#
# sep 3
##mine = [1,2,3,4,5,6,] #, at the end makes no change to the list
##reduced = mine[::2], #, after the end of the assignment makes reduced a tuple
###reduced[0]=10 #tuple' object does not support item assignment
##print(reduced)
#
#sep 1
##print((lambda a,b:a*b)(5,4)==True)#False, Immediate Invokation of Function
##print((lambda a,b:a*b)(5,4)-True)#True is considered integer 1.
#
#sep 2
##s = "\n"
##print(s.split())#splits at empty space " " or user provided seperator
##print(s.splitlines()) #splits at new line character "
### pour comparison
##s= "la tourneuse de pages"
##print(s.split())
##print(s.splitlines())
#
##identified = ["Bird","plane","superman"]
##def logic(observed):
##    for item in identified:
##        if observed.lower()==item.lower():
##            return observed
##    else:
##        return "meh" #function returns meh as it is the last return statement
##print(logic('ufo')) #meh
#sep 1
#
##def outer(x):
##    def inner():
##        return x
##result = outer(6) #no output outer function doesnt have a return statement
#
##def outer(x):
##    def inner():
##        return x
##    x = x+5
##result = outer(6) # no output outer function doesnt have a return statement
#
##def outer(x):
##    def inner():
##        return x
##    x = x+5
##    return inner
##result = outer(6) #<function outer.<locals>.inner at 0x7f229921b268>
#another
##def f(x):
##    return (x+3)*5
##y = f(3) #30, you dont need to do y() to get output, that is the whole point of this code
#
def outer(x):
    def inner():
        return x
    x = x+5
    return inner
result = outer(6)
##print(result()) #11, putting this parenthesis after result ie result() is the key here
#
#aout 25, dictionary update
##d = dict(mom=21, dad =23, kid=2)
##def fun_d(d):
##    d = {"grandpa":45,"grandma":46}
##    return d #no scope variable update
##print(fun_d(d)) #{'grandpa': 45, 'grandma': 46} 
#
#print(-1%2) #1
#print(-3%2) #1
##s = {3,2,6,7,2,5,3,1,-1,4}
##n = [val for val in s if val%2!=0]
##print(s,"\n", n)
#
#aout 25,@python_tip
##lookup = {"cz":"czech","de":"germany",'fi':'finland'}
##result = [x for (x,lookup[x]) in ["ab","bc"]] #[a,b]
##res = [x for (x,lookup[x]) in ["ab","bc","cd",'de'] if x in lookup] #[a,b,c,d]
#
import string as s
s = {c for c in s.ascii_lowercase if c in "aeiou"} #not clear yet
print(s)
#
##a =4
##if a<0: #no output
##    print("Negative")
##    print(a)
#aout 25 isinstance(bool)
##x = [1,True,[],0,"",False,{},(),"Choisir Pas", None]
##y = [True, 1, "Python", 5, False, {}, True]
##integer_count, boolean_count = 0,0
##for item in x:
##    if isinstance(item,bool):
##        print(item, "bool")#True, False
##        boolean_count +=1   
##    elif isinstance(item,int):
##        integer_count +=1
##        print(item, item**2)
##print(f"{integer_count },{boolean_count}", "\n")#2,2
###
###aout 25 isinstance(bool) different behavior when count isnt used
##x = [1,True,[],0,"",False,{},(),"Choisir Pas", None]
##for item in x:
##    if isinstance(item, bool):
##        print(item, "bool", item*item)
##    elif isinstance(item,int):
##        print(item, item*item) #True and False are considered integers and their squares are 1 and 0

#aout 25 format
#print("{2},{1},{0}".format(*"abc"))#outputs cba, abc unpacked into a tuple
#
#aout 22 zip with list
##numbers = [number for number in range(1,6)]
##letters = ["a","b","c"]
##print(list(zip(numbers,letters)))#[(1, 'a'), (2, 'b'), (3, 'c')]
#
#aout 25 nested lambdas
##ans = lambda x:(lambda y:(lambda z:z))
##result = ans(10)(20)(30)
##print(result) #as expected 30 but lambda doesnt work till you have provided all the three values x,y,z
#
#aout 22, 2023 attributs of a function
##def person():
##    person.language = "Francais"
##    def language():
##        return person
##    return language()
##person.language = "English"    
##print(person())    #<function person at 0x7f33d91b8730>
#

#python takes last value for an object
##class Random:
##    pass
#r = Random() #do dir(r)
##class Random1:
##    "takes a random number and squares it"
##    def __init__(self,number):
##        self.number = number
##    def square(self):
##        return self.number*self.number
##rs = Random1(5)#do dir(rs)
##class Random: #now random class doesnt get mixed with earlier Random class with r object, but if objects are not instantiated, the later Random class will be taken up
##    "checking order"
##    def __init__(self):
##        pass
##        #self.number = number
##    def do_nothing(self):
##        print("did nothing")
###rdn = Random()
##rp = Random()        #do dir(rp), the class picked up by the object was later one
#

#
#aout 22,2023 slicing
#l = [1,2,3,4]
#print(l[4])#IndexError: list index out of range
#print(l[-1])#4, reverse indices start from -1
#print(l[-4])#1
#print(l[1:4:-1])#[]
#print(l[0:5])#[1,2,3,4]
#print(l[5:0])#[]
#print(l[-5])#index out of range
#
#aout 22,2023
#print(10+int("5"))#15
#
#print(not None) #True
#print(not None is False) #True BECAUSE
#
#print({range(3)}) #{range(0,3)} a range object is a range object till its passed to a DS such as list, tuple, enumerate etc
#
##l = [1,2,3,4]
##another = l #another and l share same id
##l.extend({})#extend works on iterable and hence there's nothing extended to l
###l.append({}) #l = [1, 2, 3, 4, {}] as append works on element level
##another[0] = l.extend({})#another = [None, 2, 3, 4] as l = l.extend() is a Nonetype
#print(all(l)) #False as None!=True
#print(any(l)) #True
#print(all(l) and any(l))
#
##a = {"Pyt":"hon"}
##b = {"hon":"Pyt"}
##c = ""
##import itertools, functools
##prod = itertools.product(a,b)
##for element in itertools.product(a,b):#note itretools.product
##    c = functools.reduce(lambda x,y : x+y, element)
##print(c)
#
##def my_fun():
##    Ellipsis
#
def dict_fun():
    dz = {1:"Java",2.0:"Python",2:"JavaScript"} #output Javascript
    return dz, dz[2.0] #https://twitter.com/RealBenjizo/status/1693684908198084746?s=20
#
##de = dict(enumerate([10,20,30],1))
##print(20 in de) #False
##print(20 in de.values()) #true
#
##def f(a=2,b=3,d={}):
##    d[a] = b
##    return d #Python resolves the reference to name of a default parameter in the scope of a function only once, when it is defined and not every time it is called. 
##print(f())#{2: 3} #https://www.geeksforgeeks.org/python-scope-resolution-when-a-function-is-called-or-defined/
##print(f(4,5))#{2: 3, 4: 5} python loads functions,variable first time the code is run and not every time

    
#
##l = [number for number in range(1,6)]
##l[:5]=set(l[1:]) #assignment later changes original l and l takes its element from set
##
#print("|".join(str(n*n+n) for n in range(5)))
##
#print(False in range(-3,3)) #checks if there's a single false which is there because of 0
#print(False == False in [False]) #true
#
##st = {False}
##if st:
##    print(True) #output is True because st is a set, not a boolean
##else:
##    print(False)
#
##print(st==True)#False
##print(st==False)#False
##print(st==None)#False st is a set, not true, false or none
##
##print([False]==False) #False #same goes for 0 or [0,False]
##print([False]==True) #False
##print([False])==None) #False
###
##print(any([True,False]))#True
##print(any([False,False]))#False
##print(all([False,False]))#False
##print(all([True,False]))#False
#put different values in x such as [1],[0],[True,False],[False,False] to check working of all and any
##x = [False,False]
##print(any(x))
##if all(x):
##        print(x)
#
my_str = "" #check truthiness my_str == True #output False
my_bool = True or False
my = not my_str
#print(my == my_bool)
#
##z, g = 4,4 #both share same id
##print(z is g) #True
#
d = dict(a=1, b=2)
#print(2 in d) #output false
#print("b" in d) #output true
#
str1 = "J adore Python"
str1.replace("adore", "aime").split()
#
str2 = str1 #both str1 and str2 have the same id and are indeed the same objects
#
def fun(entered):
    if type(entered) == (list or tuple):
        return entered
    else:
        return "wrong data type"

s = "simple mais génial, écrivez une critique plus tard" #sort this sentence

#
a = "in"
b = "king" #a is in b but list(a) is not in list(b)

parenthesis_list = ")()())()()()()())()()((("
#p = print(list([number for number in range(5)])) # p is lass None type, a none object
#
#print(set((1,4))==set((4,1))) #output true
if (1,3)!=(3,1) and set((1,3)) == set((3,1)):
    #print("out") #output out
    pass
#    
a, b = (1,3), (3,1)
##print(a!=b and set(a)==set(b)) #true
##print(a==b and set(a)==set(b)) #False
##print(a==b or set(a)==set(b))# True
##print(a!=b or set(a)==set(b)) #true
#

##x = [1,2,3] #x and y do not share same id as assigned separately
##y = [1,2,3]
##a = "hello"
##b = "hello"
###print(x is y, a is b) #False, True
#
##x,y = [1,2,3],[1,2,3]
##a,b = "hello","hello"
##print(x is y, a is b) #False, True               






"""Is winning more important than peace for you

There are three ways to tackle things 
Wait for time, luck and god to solve it
Sit calmly, calculate and do as little or as much as you can do
Be desperate narrowing your vision, completion depends on the difficulty of the problem, not your desperation

Dopamine, excuses, amygdala, trivial stuff, unproductive habits are hard to refuse but it sees itself out if there's something more important than dopamine check if you have anything more important when you feel urge for dopamine (Marshmallow experiment)"""


   

            
