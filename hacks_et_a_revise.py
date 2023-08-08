import ds_operations
global_variable = 20

class UsefulHacks:
    def __init__(self, l=ds_operations.dso.ds1,s=ds_operations.dso.s): #passing values from another file
        self.l = l
        self.s = s
        self.gv = global_variable #a class can access outside(current scope's) variable directly
    def range_to_generate_floats(self):
        temperatures = [temp/10 for temp in range(20,480,5)]
        return temperatures
    def list_modification_in_place(self):
        l = [number for number in range(global_variable)] # a function can access outside global variable directly
        l[:] = [number**2 for number in l if number%2==0]
        return l  
    def string_reverse(self):
        "cant use reversed(s) on string as strings are immutable"
        reversed_string = self.s[::-1]
        return reversed_string
    def slicing(self):
        "[start,end, step]"
        reversed_string = self.s[::-1] 
        return reversed_string
    def slicing1(self):
        example = self.s[::-3]
        return example #note that first element is always included in slicing                                                        
    def if_mutiple_together_and_one_liner(self):
        "match if a string has a character"
        char = str(input("enter a character"))
##        if char in self.s: #combining multiple ifs by using keyword in
##            return char
##        else:
##            return f"{char} not there"
        return char if char in self.s else "voila" #this is one liner for above if else
uh = UsefulHacks()

class UsefulKeywords:
    "not, in, is, id, del"
    def __init__(self,l=[],char="s",sen="ambition de quoi, croire en quoi, sa paix du moment, pas la recherche de quelque chose incluant la paix"): 
        self.l = l
        self.char = char
        self.sen = sen
    def not_et_in(self,input_char):
        return input_char if input_char not in self.sen else not self.l
    def not_et_in2(self,input_char):        
        return ("empty" if input_char not in self.sen else not "not empty")
uk = UsefulKeywords()

class BuiltIns:
    "divmod, eval, exec"
    def __init__(self,l=[numbers for numbers in range(1,6)],char="s",sen="ambition de quoi, croire en quoi, sa paix du moment, pas la recherche de quelque chose incluant la paix"):
        self.l = l
        self.char = char
        self.sen = sen
bi = BuiltIns()

class ExamplesToRevise:
    def __init__(self,l=[numbers for numbers in range(1,6)],s="connards"):
        self.l = l
        self.s = s
    def sum_nested_for_loop(self): #A VERY GOOD EXAMPLE
        "https://twitter.com/RealBenjizo/status/1687160527129100299?s=20"
        result = sum((x for x in (y+1 for y in self.l)),10)//3
        #return (x for x in (y+1 for y in self.l)) #nested for loop output [2,3,4,5,6]
        return result #sum first adds up all elements in list output by nested for loop and then adds 10 to the total
er = ExamplesToRevise()

class HacksExamples:
    def __init__(self, l=[], s= "J adore Python"):
        self.l = l
        self.s = s
    

        
#ones that can't be written in a class
#use of next
dso = ds_operations.DSOperations()
def nextsublists(t=(1,2,3)):
    sublists = []
    for i in range(len(t)+1):    
        for j in range(1,len(t)+1):
            print(i,j)
            #if j>i:
            #sublists.extend(t[i:j]) [[1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2]]
            sublists.append(t[i:j])
            yield sublists

l = iter(nextsublists())    #now you can do next(l) to see items one by one, useful when you want to see how a loop is running
#most hacks are from problems posted on twitter by benjamin benett alexander and rohan paul
print([1,2,3] and [1,2,3]) #and returns the first false value or the last true value
print([1,2,3] is [1,2,3]) # is checks if ids of the objects are same
print([1] and 2 and 0) #checking more than two values with and
print(0 or 1) #first true object or last false object if all are false
print(0 or [] or 2)
print(([1,2,3]))#parenthesis doesnt make it a tuple
print(round(1.5))#if value is exactly in middle rounds up to the nearest even number hence 2
print(round(2.5))#ans again 2
#a function picks up global variable itself
def multiply(x):
    x*=1
    return value*10 #value is undefined local variable hence error
value = 10
value = multiply(10) #function will take outside global variable and process it


      

