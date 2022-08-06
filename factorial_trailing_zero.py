# https://mathworld.wolfram.com/Factorial.html
# Z = Sum (k = 1 -> k_max)floor[(n / (5 ** k))],
# k_max = log(n, 5)

import math

def zeros(n):
    
    if n == 0:
        return 0
    else:
        k_max = int(math.log(n, 5))
        return (sum(int(n / (5 ** k)) for k in range(1, k_max+1)))