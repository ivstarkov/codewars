n = 178008001788

def next_smaller(n):
    list = [x for x in str(n)]
    for i in range(len(list) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]
                list[j + 1:] = sorted(list[j + 1:], reverse=True)
                
                return int("".join(list))
    return -1


print(next_smaller(1027))