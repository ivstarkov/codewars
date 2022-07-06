array = [[1,2,3,1],
         [4,5,6,4],
         [7,8,9,7],
         [7,8,9,7]]


width = len(array[0])
height = len(array)
list = array[0]

list.append(array[1][2])
array[2].reverse()
list.extend(array[2])
list.append(array[1][0])
list.append(array[1][1])

