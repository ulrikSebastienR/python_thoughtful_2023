word = "random"

l = []
for i in range(len(word)):
	if i%2 ==0:
		l.append(word[i])

sen = "les semaine precedement j view bonne mere et petit arrangement avec les morts"
words = sen.split()

#seperate out 
l_even, l_odd, l_final = [], [], []
for i in range(len(words)):
    if i%2 == 0:
        l_even.append(words[i])
    else:
        l_odd.append(words[i])





