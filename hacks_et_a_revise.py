import ds_operations_et_conversions as ds
global_variable = 20

class UsefulHacks:
    def __init__(self, l=ds.dso.ds1,s=ds.dso.s): #passing values from another file
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
    "not, in, is, id, del, hash"
    def __init__(self,l=[],char="s",sen="ambition de quoi, croire en quoi, sa paix du moment, pas la recherche de quelque chose incluant la paix"): 
        self.l = l
        self.char = char
        self.sen = sen
    def not_et_in(self,input_char):
        return input_char if input_char not in self.sen else not self.l
    def not_et_in2(self,input_char):        
        return ("empty" if input_char not in self.sen else not "not empty")
    def assignment_and_id(self):
        "l1 = l2 makes l1 and l2 to share same id making changes in one reflected in another"
        l1 = [1,2,3]
        l2 = [1,2,3]
        l3 = l1
        print(id(l1), id(l2), id(l3)) #139928290137352 139928274760904 139928290137352
uk = UsefulKeywords()

class BuiltIns:
    "divmod, eval, exec"
    def __init__(self,l=[numbers for numbers in range(1,6)],char="s",sen="ambition de quoi, croire en quoi, sa paix du moment, pas la recherche de quelque chose incluant la paix"):
        self.l = l
        self.char = char
        self.sen = sen
    def ord_to_convert_string_to_number(self, s = "1234"):# problem statement NOT CLEAR YET 
        "ord gives ascii value and can be used to convert numbers input as string without using int"
        l = []
        for char in s:
            l.append(ord("char")-ord("0"))
        return l        
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
dso = ds.DSOperations()
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


            
      

