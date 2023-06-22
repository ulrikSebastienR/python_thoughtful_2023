#list all files in a directory
import os
os.chdir("/home/normal/python_thoughtful/trial")
print(tuple(os.walk(os.getcwd())), "\n")
for root, dirs, files in os.walk(os.getcwd()):
    print(f"root is {root}")
    print(f"directories in {root} are {list(dirs)}")
    print(f"files in {root} are {list(files)}", "\n")
    for d in dirs:
        x = str(os.path.join(root, d))
        print(f"x is {x}", "\n")
        for rootx, d1, filesx in os.walk(x):
            list_of_files, l = [], []
            for file in filesx:
                print(os.path.join(rootx, file), "\n")
                y = str(os.path.join(rootx, file))
                l.append(y)
                #works correct so far, now to store all files in a list
print(l)                
            



'''print('\n', "down to top os.walk")

for root, dirs, files in os.walk(os.getcwd(),topdown=False):
    print(f"root is {root}")
    print(f"directories in {root} are {list(dirs)}")
    print(f"files in {root} are {list(files)}")'''
