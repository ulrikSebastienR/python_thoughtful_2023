print("no longer needed")
import os
print("cwd is", os.getcwd())
os.chdir("/home/normal/python_thoughtful/trial")
print("now cwd is", os.getcwd())
for root, dirs, files in os.walk(os.getcwd()):
	print(f"root is {root}")
	for d in dirs:
		print(f"joined root and directory is {os.path.join(root,d)}")
		for file in files:
			print(f"file level is {os.path.join(root, d, file)}")
