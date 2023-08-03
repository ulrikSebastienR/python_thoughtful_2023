#zig zag pattern from a file named no. 5 #do combinations by removing duplicates from permutations#longest closing parentheses#merge intervals#arrange a list on the basis of another list#os.path.isfile()
zigzag = "/home/normal/python_thoughtful/dir_pour_experimentation/trial2/zigzag.py"
path2 = "/home/normal/python_thoughtful/solutions_leetcode_etc.tex"
path3 = "8.py"

class FileOperations:
    def __init__(self, path=zigzag):
        self.path = path
    def read_method(self): #outputs contents in a string
        with open(self.path) as f:
            contents = f.read()
        #print(contents)
        return contents
    def read_lines(self): #outputs all lines in a list
        with open(self.path) as f:
            return f.readlines()
    def line_with_line_number(self):
        with open(self.path) as f:
            for count, line in enumerate(f.readlines()):
                print(count, line)
    def zigzag_pattern_string(self):
        s = self.read_method()
        return s
    def merge_sublists_element_wise(self):
        s = self.read_method()
##        for element in s: #considering all sublists are same size
##            traverse = max(len(element))
##            
##            for i in range(len(
    def read_zigzag_pattern_from_file(self):
        with open(zigzag) as f:
            s = f.read()                     
            output = []
            output = [item for item in s if item!="\n" or item!= " "]
##            for i in range(len(l)-1): #-1 because split picks up last line as blank
##                output.append(l[i])
##                output[:] = [item for item in output if item!=" "]
            return output
    def merge_files(self, path2=path2):
        with open(self.path) as f1:
            f1_contents = f1.read()
        with open(path2) as f2:
            f2_contents = f2.read()
        merged = "added from command line" + f1_contents + f2_contents
        with open(path3, "w") as f3:
            f3.write(merged)
        with open(path3, "r") as f4:
            output = f4.read()
        return output
        
fo = FileOperations()

s = "simple mais génial, écrivez une critique plus tard" #sort this sentence
  

#char = str(input("enter a char"))
def not_et_in(char):
    return ("empty" if char not in s else not "not empty")


#f = open(path2)
#f.close()
a,*b,c = ["car","dog","tiger","lion"]
item = b
s = fo.zigzag_pattern_string()
lengths = []
lines = s.split("\n")
lines[:] = [item for item in lines if item!=""]
for element in lines:
    lengths.append(len(element))

"It is possible for courts to deliver a non guilty verdict in absentia but does it hold true for humans too or do they even consider the question"

           
    

            
