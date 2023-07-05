#you can comare anything in python
n1, n2 = 5,10
l1 = l2 = [char for char in "demain"]
s1,s2 = "madam", "madamoiselle"
t1 = t2 = (1,2)

def compare_anything(x,y):
    "pass any two data structures to check if they are equal"
    flag = False
    if x == y:
        flag = True
    return flag

#compare if two files have same content or not
f = open("pour_reading.tex")
word_pour1 = word_pour = f.read()
f.close()

f = open("openquestions.tex")
word_other = f.read()
f.close()
