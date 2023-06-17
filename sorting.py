#various sorting in python
#without using inbuilt function

#sort a list
l = [31, 23, 83, 12, 86, 97, 34, 18]
l_s = []
while len(l)!=0:
    l_s.append(min(l))
    l.remove(min(l))


