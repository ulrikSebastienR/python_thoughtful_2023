#list comprehension,
l = [n for n in range(20) if n%2==0]

#dict
d1 = {"a":1, "b":2}
d2 = {"c":3, "d":4}
d = {**d1, **d2} #merge

#not working
'''l = []
l = [n for n,i in zip(range(1,13), range(2,n)) if n%i==0]'''
