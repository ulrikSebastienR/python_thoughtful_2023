import ds_operations

class UsefulHacks:
    def __init__(self, l=ds_operations.dso.ds1,s=ds_operations.dso.s): #passing values from another file
        self.l = l
        self.s = s
    def range_to_generate_floats(self):
        temperatures = [temp/10 for temp in range(20,480,5)]
        return temperatures
    def list_modification_in_place(self):
        l = [number for number in range(5)]
        l[:] = [number**2 for number in l]
        return l  
    def string_reverse(self):
        "cant use reversed(s) on string"
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
    "not, in, is, id"
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
    def __init__(self,l=[],char="s",sen="ambition de quoi, croire en quoi, sa paix du moment, pas la recherche de quelque chose incluant la paix"):
        self.l = l
        self.char = char
        self.sen = sen
bi = BuiltIns()
        
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


