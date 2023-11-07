#do combinations by removing duplicates from permutations#longest closing parentheses#merge intervals#group patterns in a number such as 123456123456123456123456123456
# an empty hash means starting of a new snippet
#nov 5
##def fun(arr:list):
##    gen = (name for name in arr if len(arr)>=3)
##    arr = ["Peter", "mary"]
##    return list(gen)
##arr = ["Joe","Peter", "Paul"]
##print(fun(arr)) #[], in the return statement gen is invoked again which bypasses the arr that was presented as an argument to the function
###nov 5
##def fun(x):
##    y = x*20
##    x = "a"
##    return y #here y = 40 as there is nothing modifying the already computed output y 
##print(fun(2)) #40
###
##def fun(x):
##    def inner(x):
##        y = x*20
##        return y
##    x = "a"
##    return (inner(x)+x),len(inner(x)+x) #now once again argument is altered inside the function definition
##print(fun(2)) #('aaaaaaaaaaaaaaaaaaaaa', 21)
#nov 5
##x = ["ab", "cd"]
##for i in x:
##    i.upper()
##print(x) #["ab","cd"] as strings are not modified by the iterator 
#nov 4
#print(2^3) #output is 1, caret character python output 1 2=0010, 3=0011 2 XOR of 3 = 1
##set1 = {45,23,56,98,75,12,30}
##set2={44,12,33,30,23}
##print(set1^set2) a-union-b minus a-intersection-b ie non common elements of a and b
#
#nov 3
#l = [1,2, ,4] #invalid syntax 
#print(l)
#print(" ".join(str(item) for item in l))
#
#nov 1
##l1, l2 = [], []
##d1, d2 = {},{}
##s1, s2 = set(), set()
##print([]==[], id(l1), id(l2), l1==l2) #True 139746680490056 139746680489544 True
##print({}=={}, id(d1), id(d2), s1==s2) #True 139746674370816 139746665829288 True
##print(set()==set(), id(s1), id(s2), s1==s2) #True 139746678954920 139746665687752 True
#oct 15
##t = (1,2,[3,4],(5),{6,7,8})
##print(t[3]) #5, not the tuple (5)
#oct 14
#c = dict(a=23,b=89,b=66) #keyword argument repeated, cant assign dictionaries with keys repeated
##l14 = [20,40,60,80]
##l14[1:4] = []
##print(l14)
#
##c = {1:23, 2:89,2:66}
##print(c.pop(2), c) #66 {1: 23}
#
#oct 3
##x = ['1']
##x.extend('234')
##print(x) #['1', '2', '3', '4']
#oct 2
#print([1,2]*-1) #[]
#sep 30
##print([1,2,3]*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3] #123123123 #(1, 2, 3, 1, 2, 3, 1, 2, 3)
##print('123'*3)
##print((1,2,3)*3)
##print({1,2,3}*3) #error 
#sep 30
##t1,t2 = (1,2,4,3),(1,2,3,4)
##print(t1<t2)#False
#sep30
##my_string = "mindfulness activates frontal lobe and makes your decisions better"
##for i in range(len(my_string)):
##    my_string[i].upper()
##    print(my_string[i], " ", my_string[i].upper())
##print(my_string) #no change as string is immutable
#sep 29
##my_string = "world"
##i = "i"
##while i in my_string:
##    print(i, end=" ") #none as there is no "i" in my_string
#sep 29
##print(not None) #True
##print(""==True) #False
##print(not None != "") #False
#sep 28
##abc = [num for num in range(5)]
##print(abc[10:]) #[], not an error
#sep 27
##i = 1
##while True:
##    if i%007=0:
##        print(i) # ERROR: invalid token
# sep 13
##tuples = ((1,'a'),(2,'b'),(3,'c'))
##my_dict = dict(tuples)
##zipped = zip(my_dict)
##l = list(zipped) 
# crazy program
##a = [1,2] #https://twitter.com/CodingComputing/status/1697870989718139095
##b = [3,4,a]
##a.append(b)
##print(a) #[1, 2, [3, 4, [...]]]
##print(b) #[3, 4, [1, 2, [...]]]
#
#sep 7, 2023
##items = [1,2,3] #all three have different ids
##numbers = [1,2,3]
##nos = numbers.copy()
##items[0] = 0 #does not change nos as nos is a copy of items, however changes items
##print(items, id(items))
##print(numbers, id(numbers))
##print(nos, id(nos))
##def add_value(items, value):
##    return items + value
##def put_value(items, value):
##    items.append(value)
##    return items
##value = [4]
##print(add_value(items,value)) #+ concatenates but does not change the original object
##print("original items after + operator", items)
##print(put_value(numbers,value))# appending changes a list 
##print("original numbers after appending", numbers)
##def plus_operator(items, value):
##    return items + [value]
##value = 4
##print(plus_operator(items,value))
##print(plus_operator(nos, value))
##print(items)
##print(numbers)
##print(nos)
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

my_lam = lambda x: x**2 if x%2==0 else x
l = [ num for num in range(20)]
f = filter(lambda x:x%2 == 0, l)
m = map(my_lam, l)





"""Is winning more important than peace for you

There are three ways to tackle things 
Wait for time, luck and god to solve it
Sit calmly, calculate and do as little or as much as you can do
Be desperate narrowing your vision, completion depends on the difficulty of the problem, not your desperation

Dopamine, excuses, amygdala, trivial stuff, unproductive habits are hard to refuse but it sees itself out if there's something more important than dopamine check if you have anything more important when you feel urge for dopamine (Marshmallow experiment)"""


   

            
