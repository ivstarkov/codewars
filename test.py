a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

a1.sort()
a2.sort()

temp = list(map(lambda a : a ** 2, a1))

print(temp)
print(a2)
print(temp == a2)