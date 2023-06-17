#attempt 2 at Capitalize words of a sentence or title case, print statements are not needed as output can be directly viewed in python shell or pyzo
sen = "petit arrangment avec les morts , 1993"
words = sen.split()
#print(words)

#simplest method
sen_t = sen.title()

#lets do it using loop and only "upper" method

#capitalize only one word
l = [char for char in words[0]]
l[0] = l[0].upper()
word = ("").join(l)


#now nesting 2 for loops for entire sentence
words_caps = ""
for word in words:
    l = [char for char in word]
    l[0] = l[0].upper()
    word = ("").join(l)
    words_caps += word + " "
#errors remaining, terminate the trailing space
#making sentence appropriate case would be difficult    
# changing case of alternate word

