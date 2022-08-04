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
    # check rows:
    for i in range(9):
        print(sum(puzzle[i])) 
    print("-------")

    # rotate and check rows again
    rotated_puzzle = list(zip(*puzzle[::-1]))
    for i in range(9):
        print(sum(rotated_puzzle[i]))
    print("-------")

    # check lil squares
    for i in range(9):

        



check(puzzle)

    
    