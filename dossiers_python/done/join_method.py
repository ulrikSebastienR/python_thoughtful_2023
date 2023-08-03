#change first alphabet of a word to upper case using join method
i = "this"
l = list(i)
l[0] = l[0].upper()
print(l)
#method 1
s = ""
i1 = s.join(l)
print(i1)

#method 2
i2 = ("").join(l)
print(i2)

