import math

def decompose(n):
    list = []
    x = n ** 2
    while x > 0:
        #print("======")
        if x == n ** 2 and x > 1:
            #print("+")
            rest = x - math.isqrt(x - 1) ** 2
            list.append(math.isqrt(x - 1))
            #print(math.isqrt(x - 1))
            #print(rest)
        else:
            #print("-")
            rest = x - math.isqrt(x) ** 2
            list.append(math.isqrt(x))
            #print(math.isqrt(x))
            #print(rest) 
        x = rest
        #print("======")





    list.reverse()
    return list

print(decompose(50))

#print(11 ** 2 - math.isqrt(11 ** 2 - 1) ** 2)