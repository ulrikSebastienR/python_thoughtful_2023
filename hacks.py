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
    def if_mutiple_together_and_one_liner(self):
        "match if a string has a character"
        char = str(input("enter a character"))
##        if char in self.s: #combining multiple ifs by using keyword in
##            return char
##        else:
##            return f"{char} not there"
        return char if char in self.s else "voila" #this is one liner for above if else
uh = UsefulHacks()

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


