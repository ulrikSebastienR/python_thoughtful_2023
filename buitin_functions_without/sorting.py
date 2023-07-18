#various sorting in python
#without using inbuilt function

#sort a list
l = [31, 23, 83, 12, 86, 97, 34, 18]
l1 = [31, 23, 83, 12, 86, 97, 34, 18]
l_s = []
while len(l)!=0:
    l_s.append(min(l))
    l.remove(min(l))

#sort a dict by keys

l2 = [char for char in "abcdefgh"]
d = dict((k,v) for k,v in zip(l1,l2))
keys = [i for i in d.keys()]
keys1 = [i for i in d.keys()]
l_keys = []
while len(keys1)!=0:
    l_keys.append(min(keys1))
    keys1.remove(min(keys1))
d = dict((k,v) for k,v in zip(l_keys,l2))  
    

#counting without len
l = [i for i in range(0,100,5)]
i = 0
for item in l:
    i += 1

i = 0
f = open('3.py')
for line in f.readlines():
    print(line)
    i += 1
