array = [[1,2,3],
         [1,2,3],
         [1,2,3]]

# Initialize list
s = []
while array:
    # 1st row
    s.extend(array[0])

    # Delete written row from array
    array.pop(0)

    # Rotate array
    array = list(zip(*array))[::-1]
print(s)
