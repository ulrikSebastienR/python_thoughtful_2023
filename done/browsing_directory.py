#list all files in a directory, chaque line dans se program est correct
import os
os.chdir("/home/normal/python_thoughtful/dir_pour_experimentation")
print(tuple(os.walk(os.getcwd())), "\n")

#simple
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        print(os.path.join(root, file))
    print("----")

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
                print(os.path.join(rootx, file), "\n")
                #works correct so far, now to store all files in a list
                y = str(os.path.join(rootx, file))
                s.add(y)
                
print(list(s),"\n", len(s))                
            



'''print('\n', "down to top os.walk")

for root, dirs, files in os.walk(os.getcwd(),topdown=False):
    print(f"root is {root}")
    print(f"directories in {root} are {list(dirs)}")
    print(f"files in {root} are {list(files)}")'''
