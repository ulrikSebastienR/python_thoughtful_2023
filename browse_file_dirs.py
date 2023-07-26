import os

class BrowseDirectory:
    "browses a directory to list all files in the directory"
    def __init__(self, path):
        self.path = path
    def files(self):
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                yield os.path.join(root, file)
bd = BrowseDirectory(os.getcwd())

class FileOperations:
    "reading and writing on files"
    def __init__(self, file):
        self.file = file
    def proper(self):
        f = open(self.file)
        return f.read() 
        f.close()
    def proper_using_with(self):
        with open(self.file) as f:
            return f.read()
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
file = os.path.join(os.getcwd(),"openquestions.tex")    
fo = FileOperations(file)

s = "  ram shiva "


                                   
                                   
