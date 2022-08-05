puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    return puzzle


def check(puzzle):
    test_set = {1,2,3,4,5,6,7,8,9}
    # check rows:
    for i in range(9):
        if set(puzzle[i]) != test_set:
            return False

    # rotate and check rows again
    rotated_puzzle = list(zip(*puzzle[::-1]))
    for i in range(9):
        if set(rotated_puzzle[i]) != test_set:
            return False
    
    # check lil squares
    for i in range(0,7,3):
        for j in range(0,7,3):
            if (sum(puzzle[j][i:i+3])+sum(puzzle[j+1][i:i+3])+sum(puzzle[j+2][i:i+3])) != 9:
                return False

    return True

print(check(puzzle))

    
    