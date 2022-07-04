a1 = [5, 4, 2]
a2 = [25, 16, 4]

try:
    temp = list(map(lambda a : a * a, a1))
    temp.sort()
    a2.sort()

except:
    print(False)