n = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]

def solution(args):
    k = 1
    for i in range(1,len(args) - 1,1):
        if args[i - 1] + k == args[i] and args[i] + 1 == args[i + 1]:
            args[i] = ""
            k += 1
        else:
            k = 1
        
    return args

print(solution(n))