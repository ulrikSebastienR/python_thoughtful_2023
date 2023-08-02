#zig zag pattern from a file named no. 5 #do combinations by removing duplicates from permutations#longest closing parentheses
zigzag = "/home/normal/python_thoughtful/dir_pour_experimentation/trial2/zigzag.py"
path2 = "/home/normal/python_thoughtful/solutions_leetcode_etc.tex"
path3 = "8.py"

class FileOperations:
    def __init__(self, path=zigzag):
        self.path = path
    def read_method(self): #outputs contents in a string
        with open(self.path) as f:
            contents = f.read()
        print(contents)
        return contents
    def read_lines(self): #outputs all lines in a list
        with open(self.path) as f:
            return f.readlines()
    def line_with_line_number(self):
        with open(self.path) as f:
            for count, line in enumerate(f.readlines()):
                print(count, line)
    def read_pattern(self):
        pass
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



#f = open(path2)
#f.close()
    

            
