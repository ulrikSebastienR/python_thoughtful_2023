import os
print(os.getcwd())
os.chdir("/home/normal/python_thoughtful/trial/")
print(f"current pwd is {os.getcwd()}")

for root, dirs, files in os.walk(os.getcwd()):
    print(f"root is {root}")
    print(f"in {root} directories are {list(dirs)}")
    print(f"in {root} files are {list(files)}")
# browses the tree perfectly, onto joining paths
print("\n", "# browses the tree perfectly, onto joining paths", "\n")

for root, dirs, files in os.walk(os.getcwd()):
    print(f"root is {root}")
    print(f"files in root {root} are {list(files)}")
    print(f"directories in root {root} are {list(dirs)}", "\n")
    for d in dirs:
        print(f"joined root and d is {os.path.join(root, d)}")
        x = str(os.path.join(root,d))
        print(f"x is {x}", "\n")
        """for file in os.walk(x):
            print(file)
            print(os.path.join(x,file))"""
	



