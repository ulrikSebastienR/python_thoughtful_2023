#do combinations by removing duplicates from permutations#longest closing parentheses#merge intervals#group patterns in a number such as 123456123456123456123456123456
# an empty hash means starting of a new snippet
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


   

            
