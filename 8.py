s = [char for char in "sandrine bonnaire"]

for char in set(s):
    i = 0
    for char1 in s:
        if char == char1:
            i += 1
    print(char, i)

#or

d = {}
for char in s:
    i = 0
    for char1 in s:
        if char == char1:
            i += 1
    print(char,i)
    #d.update((char,i))
    
