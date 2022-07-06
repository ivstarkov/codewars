array = [[1,2,3,1],
         [4,5,6,4],
         [7,8,9,7],
         [7,8,9,7]]


width = len(array[0])
height = len(array)

# 1st row
list = array[0]

# Right row
for i in range(1, height - 1):
    list.append(array[i][width - 1])

# Bottom row
array[height - 1].reverse()
list.extend(array[height - 1])

# Left row
for i in range(height - 2, 0, -1):
    list.append(array[i][0])

#unpack array
array.pop(0)
array.pop()
for i in range(height - 2):
    array[i].pop()
    array[i].pop(0)







