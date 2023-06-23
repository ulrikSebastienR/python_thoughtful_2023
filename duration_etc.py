#leap years in a range
i, l = 0, []
for year in range(1900, 2023):
    if year%4 ==0:
        l.append(year)
        i +=1
