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
