"""
  You're given a two-dimensional array (a matrix) of potentially unequal height
  and width containing only 0s and 1s. The matrix represents a two-toned image, 
  where each 1 represents black and each 0 represents white. 
  An island is defined as any number of 1s that are horizontally or vertically 
  adjacent (but not diagonally adjacent) and that don't touch the border of the image. 
  In other words, a group of horizontally or vertically adjacent 1s isn't an
  island if any of those 1s are in the first row, last row, first column, 
  or last column of the input matrix.

  Note that an island can twist. In other words, it doesn't have to be a
  straight vertical line or a straight horizontal line; it can be L-shaped, for
  example.
  You can think of islands as patches of black that don't touch the border of
  the two-toned image.
  Write a function that returns a modified version of the input matrix, where
  all of the islands are removed. You remove an island by replacing it with
  0s.
  Naturally, you're allowed to mutate the input matrix.</p>
  Sample Input
matrix = 
[
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]
]
Sample Output [
  [1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 1]
] 
The islands that were removed can be clearly seen here:
[
 [ ,  ,  ,  ,  , ],
 [ , 1,  ,  ,  , ],
 [ ,  , 1,  ,  , ],
 [ ,  ,  ,  ,  , ],
 [ ,  , 1, 1,  , ],
 [ ,  ,  ,  ,  , ] 
]
"""


def removeIslands(matrix):
    # Write your code here.
    # Tracked Matrix
    onesConnectedToBoder = [[False for value in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowInBorder = row == 0 or row == len(matrix[0]) - 1
            colInBorder = col == 0 or col == len(matrix) - 1
            isOnBorder = colInBorder or rowInBorder
            ## if not in the border we not check, just to focus on
            if not isOnBorder:
                continue

            if matrix[row][col] != 1:
                continue
            findTheOnesConnectedToTheBorder(matrix, row, col,
                                            onesConnectedToBoder)

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if onesConnectedToBoder[row][col]:
                continue
            matrix[row][col] = 0

    return matrix


def findTheOnesConnectedToTheBorder(matrix, startRow, startCol,
                                    onesConnectedToBoder):

    stack = [(startRow, startCol)]
    while stack:
        currentRow, currentCol = stack.pop()
        if onesConnectedToBoder[currentRow][currentCol]:
            continue
        onesConnectedToBoder[currentRow][currentCol] = True
        stack += getNeighBors(matrix, currentRow, currentCol)


def getNeighBors(matrix, row, col):
    neighbors = []
    numOfRow = len(matrix)
    numOfCol = len(matrix[row])
    if row - 1 >= 0 and matrix[row - 1][col] != 0:  # Up
        neighbors.append((row - 1, col))
    if row + 1 < numOfRow and matrix[row + 1][col] != 0:  # Down
        neighbors.append((row + 1, col))
    if col - 1 >= 0 and matrix[row][col - 1] != 0:  # Left
        neighbors.append((row, col - 1))
    if col + 1 < numOfCol and matrix[row][col + 1]:  # Right
        neighbors.append((row, col + 1))
    return neighbors


def test1():
    input = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    expected = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    actual = removeIslands(input)
    assert actual == expected


if __name__ == "__main__":
    test1()