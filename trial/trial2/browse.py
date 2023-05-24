import os
print(os.getcwd())
os.chdir("/home/normal/python_thoughtful/trial/")
print(f"current pwd is {os.getcwd()}")

for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(list(dirs))
    print(list(files))
# browses the tree perfectly, lets join paths

for root, dirs, files in os.walk(os.getcwd()):
    print(f"root is {root}")
    for d in dirs:
        print(f"joined root and d is {os.path.join(root, d)}")
        #correct so far
        for file in files:
            print("file is {file}")
            print(f"joined at file level is {os.path.join(root,d,file)}")


