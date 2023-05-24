import os
print(os.getcwd())
os.chdir("/home/normal/python_thoughtful/trial/")
print(f"current pwd is {os.getcwd()}")

for root, dirs, files in os.walk(os.getcwd()):
    print(f"root is {root}")
    print(f"in {root} directories are {list(dirs)}")
    print(f"in {root} files are {list(files)}")
# browses the tree perfectly, lets join paths
print("\n", "# browses the tree perfectly, lets join paths", "\n")

for root, dirs, files in os.walk(os.getcwd()):
    print(f"root is {root}")
    print(f"files in root {root} are {list(files)}")
    print(f"directories in root {root} are {list(dirs)}")
    for d in dirs:
        print(f"joined root and d is {os.path.join(root, d)}")
        #correct so far
        for file in files:
            print(f"file is {file}")
            print(f"joined at file level is {os.path.join(root,d,file)}")


