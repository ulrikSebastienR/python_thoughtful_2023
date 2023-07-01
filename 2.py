#swap upper and lowercases in a string
s = "VaLeRiABrUno"
#for char in s:
ss = "".join([char.upper() if char.islower() else char.lower() for char in s])   



