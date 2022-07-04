def sqInRect(lng, wdth):
    if lng == wdth:
        return None 
    list = []
    while lng > 1 and wdth > 1:
        minimum = min(lng, wdth)
        maximum = max(lng, wdth)
        wdth = maximum - minimum
        lng = minimum
        list.append(minimum)
    for _ in range(maximum - 1):
        list.append(1)
    return list

print(sqInRect(37, 14))