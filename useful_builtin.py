#enumerate
f = open("3.py")
for count,trial in enumerate(f,1):
    print(count,trial)
f.close()
#enumerate
fruits = ["banana", "apple", "mango", "orange", "malta"]
for j in enumerate(fruits, 1):
    print(j)
    
#sorted, reversed cant be used for dictionaries
#keyworded arguments
