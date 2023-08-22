import os
os.chdir('/home/normal/python_thoughtful/dir_pour_experimentation')
for root, dirs, files in os.walk(os.getcwd()):
    print(root,dirs,files)




