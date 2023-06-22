#you need to close a file or open with WITH, "w" creates a file or overwrites existing, "a" appends existing file
with open("blank.tex", "w") as f:
    f.write("written through python") #no need to close explicitly

#you need to open file every time else f.readlines would be an empty list
#print specified number of characters
f = open("openquestions.tex")
print(f.readline(15))
print("-----")
f.close()

#count number of lines in a file
f = open("openquestions.tex")
i = len(f.readlines())
#or
f = open("openquestions.tex")
j = 0
for each in f:
    j += 1
f.close()

#get all contents in a list
f = open("openquestions.tex")
data = f.readlines()
print(data)
print("-----")

#print each line with line number
f = open("openquestions.tex")
for i,line in enumerate(f.readlines(),1):
    print(i,line)
print("------")
    
#print each word
f = open("openquestions.tex")
for line in f.readlines():
    print(line)
    for word in line.split():
        print(word)
    print("-")

#still left delete a particular line or arrange words as per your choice or put space at a particular point in a file
