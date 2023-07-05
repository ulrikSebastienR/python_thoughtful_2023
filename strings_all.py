#reverse a string, you can reverse a list using l.reverse()
s = "madamoiselle"
def reverse_string(s):
    l = [char for char in s]
    l_reversed = []
    l_reversed.extend(l[len(l)-1-i] for i in range(len(l)))
    return "".join(l_reversed)
                        
def sort_string_alphabets(s):
    "sorts a string alphabetically"
    l = [char for char in "abcdedfghijklmnopqrstuvwxyz"]
    



#join

sen = "happiness is feeling so full that you get bored. dopamine is chasing after noise"
print(sen.split())
print("+".join(sen))

# string is immutable
words = sen.split()



