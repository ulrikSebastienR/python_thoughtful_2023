#count number of lines in a file
f = open("3.py")

count = len(f.readlines())
f.close()
# OR
f = open("3.py")
i = 0
for line in f.readlines():
    print(line)
    i += 1
f.close()

#print lines with line numbers
f = open("3.py")
for count, line in enumerate(f, 1):
    print(count," ", line)
f.close()



#delete particular lines of a file with python

f = open('3.py', "r")
for line in f.readlines(-1):
    print(line)
##    f.writelines("a")
##    print(line)
    #f.close()



#using with itself closes the file preventing further access
with open("openquestions.tex") as f1:
    pass #no need to close



