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
    visited = [[False for value in row] for row in matrix]

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if visited[i][j]:
                continue
            remove = traverseTheMatrix(i, j, matrix, visited)
            for coord in remove:
                matrix[coord[0]][coord[1]] = 0
    return matrix


def traverseTheMatrix(i, j, matrix, visited):
    nodeToRemove = []
    isAnIsland = True
    nodeToVisit = [[i, j, isOnBorder(i, j, len(matrix), len(matrix[0]))]]
    while nodeToVisit:
        coordToExplore = nodeToVisit.pop()
        i = coordToExplore[0]
        j = coordToExplore[1]
        onBorder = coordToExplore[2]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        nodeToVisit += getUnvisitedNeighbors(i, j, matrix, visited)
        isAnIsland = False if onBorder else isAnIsland
        nodeToRemove.append([i, j])

    return nodeToRemove if isAnIsland else []


def isOnBorder(i, j, heightMatrix, withMatrix):
    onBorder = False
    if i == 0 or j == 0 or i == heightMatrix or j == withMatrix:
        onBorder = True
    return onBorder


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    heightMatrix = len(matrix) - 1
    withMatrix = len(matrix[0]) - 1
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append(
            [i - 1, j,
             isOnBorder(i - 1, j, heightMatrix, withMatrix)])
    if i < heightMatrix and not visited[i + 1][j]:
        unvisitedNeighbors.append(
            [i + 1, j,
             isOnBorder(i + 1, j, heightMatrix, withMatrix)])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append(
            [i, j - 1,
             isOnBorder(i, j - 1, heightMatrix, withMatrix)])
    if j < withMatrix and not visited[i][j + 1]:
        unvisitedNeighbors.append(
            [i, j + 1,
             isOnBorder(i, j + 1, heightMatrix, withMatrix)])
    return unvisitedNeighbors


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