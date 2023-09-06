import os, pathlib, glob
path = '/home/normal/python_thoughtful/dir_pour_experimentation'

class BrowseDirectory:
    "browses a directory to list all files in the directory"
    def __init__(self, path):
        self.path = path
    def files(self):
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                yield os.path.join(root, file)
bd = BrowseDirectory(os.getcwd())

zigzag = "/home/normal/python_thoughtful/dir_pour_experimentation/zigzag.tex"
twitter = "/home/normal/python_thoughtful/latex/a_faire_twitter.tex"
leetcode = "/home/normal/python_thoughtful/latex/solutions_leetcode_etc.tex"
file_to_write = "trash.py"
class FileOperations:
    "reading and writing on files"
    def __init__(self, file=twitter):
        self.file = file
    def check_if_file_exists(self,file_to_check=leetcode):#checks if a file exists
##        if os.path.isfile(file_to_check):
##            return "Oui"
##        else:
##            return "Pas"
        return "File Exists" if os.path.isfile(file_to_check) else "Pas Existe"
    def load_zigzag_from_file(self,zigzag=zigzag):
        with open(zigzag) as f:
            return f.read()
    def read_zigzag_from_file(self,zigzag=zigzag):#INCOMPLETE ERROR AN EXTRA TAB SPACE AND A MISSING AND CREATE SPACE BETWEEN WORDS
        with open(zigzag) as f:
            s = f.read()
        lines = s.split("\n")
        lines[:] = [item for item in lines if item != ""]
        len_to_traverse = max(len(item) for item in lines)
        pattern = []
        for i in range(len_to_traverse):
            try:
                pattern.append(lines[0][i])
                pattern.append(lines[1][i])
                pattern.append(lines[2][i])
            except:
                pass
        pattern = [item for item in pattern if item!=" "]
        return "".join(pattern)
    def proper(self):
        f = open(self.file)
        return f.read() #read(-1) or read() will read entire file into a string while read(5) will read 5 characters from start no but lines are not separated
        f.close()
    def contents_proper_using_with(self): #output contents in a string
        with open(self.file) as f:
            contets = f.read() 
            return contents
    def read_lines(self): #output all lines in a list
        with open(self.file) as f:
            return f.readlines()#reads entire file into a list where items are different lines
    def lines(self):
        chars= lines= words = []
        f = open(file) #note works for both self.file and file as a class can directly take outside variable
        contents = f.read() #you can do f.read() only once 
        lines = contents.split("\n")
        return lines
    def count_lines(self):
        i = 1
        with open("openquestions.tex") as f:
            for line in f.readlines():
                print(i, line)
                i+=1
        return i
    def count_characters(self):
        d,i = {},0
        with open("openquestions.tex") as f:
            for character in f.read():
                i+=1
                d.update({i:character})
        return d
    def words(self):
        words = []
        f = open(self.file)
        contents = f.read()
        words = contents.split()
        return words
    def merge_files(self):
        with open(self.file) as f1:
            contents1 = f1.read()
        with open(leetcode) as f2:
            contents2 = f2.read()
        merged = "these files were merged from cli using python"+contents1+contents2
        with open(file_to_write,"w") as f3: #x is to create, w is to truncate, a is to append
            f3.write(merged)
        with open(file_to_write,"r") as f4:
            return f4.read()                 
    def characters_with_newline(self):
        chars = []
        f = open(file)
        contents = f.read()
        for char in contents:
            chars.append(char)
        return chars
    def with_numbers_lines_of_file_with_enumerate(self):
        with open("openquestions.tex") as f:
            for count, line in enumerate(f,1):
                yield count, line
    def characters_of_file_with_enumerate(self):
        with open("openquestions.tex") as f:
            with count, character in enumerate(f.read(),1):
                yield count,character
    def only_chars(self):
        "characters with new line characters stripped"
        chars = []
        f = open(file)
        contents = f.read()        
        chars.extend(char for char in contents if char != "\n") #putting append will make it output saying generator object
        return chars
    def readline_vs_readlines(self):
        pass         
#file = os.path.join(os.getcwd(),"openquestions.tex")    
fo = FileOperations()

#earlier approach

s = set()

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        y = str(os.path.join(root, file))
        s.add(y)
    #print(f"root is {root}")
    #print(f"directories in {root} are {list(dirs)}")
    #print(f"files in {root} are {list(files)}", "\n")
    for d in dirs:
        x = str(os.path.join(root, d))
        #print(f"x is {x}", "\n")
        for rootx, d1, filesx in os.walk(x):
    
            for file in filesx:
               # print(os.path.join(rootx, file), "\n")
                #works correct so far, now to store all files in a list
                y = str(os.path.join(rootx, file))
                s.add(y)
                
#print(list(s),"\n", len(s))          

path1 = "/home/normal/python_thoughtful/aujourdhui.py"
with open(path1) as f:
    x = f.read().splitlines()
    

#print(os.path.isfile(path1))
                                   
                                   
