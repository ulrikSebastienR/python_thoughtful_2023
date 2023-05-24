import os
print(os.getcwd())
print("this program lists everything")
print("you can verify with tree -a 'folder' ")
for root, dirs, files in os.walk(os.getcwd()):
    print("root is", root)
    print("directories are", list(dirs))
    for d in dirs:
        print(f"in root {root} directory is {d}")
        for file in files:
            print(f"in root {root} dir is {d} and file is {file}")

print("\n", "trying out joining path")
for root, dirs, files in os.walk(os.getcwd()):
    for root in root:
        for d in dirs:
            for file in files:
                print(f"in {os.path.join(d,file)} ")



