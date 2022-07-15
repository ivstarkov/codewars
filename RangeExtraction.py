n = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]

def solution(args):
    for x in args:
        # Find length of consecutive sub-string
        i = args.index(x)
        l_counter = 1
        while i < len(args) - 1 and args[i] == args[i + 1] - 1:
            l_counter += 1
            i += 1
        # Place "-" instead of sub string
        if l_counter > 2:
            args[args.index(x) + 1: args.index(x) + l_counter - 1] = "-"

               
        
    temp = ','.join(str(x) for x in args)
    return temp.replace(",-,", "-")

print(solution(n))