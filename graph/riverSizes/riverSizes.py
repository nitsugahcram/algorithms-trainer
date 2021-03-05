"""You are given a two-dimensional array of potentially unequal height and width. 
It contains only 0s and 1s. This array represents a map: 0s are land, and 1s are water. 
A "river" on this map consists of any number of contiguous, adjacent water squares, 
where "adjacent" means "above", "below", "to the left of", or "to the right of"
 (that is, diagonal squares are not adjacent).
Write a function which returns an array of the sizes of all rivers represented in the input matrix. 
Note that these sizes do not need to be in any particular order.

const input = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
];

riverSizes(input); // returns [1, 2, 2, 2, 5]

"""


# Time: O(w*h), Space: O(w*h)
def riverSizes(matrix):
    # Write your code here.
    sizes = []
    # Initialize a Track Matrix
    visited = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverserNode(i, j, matrix, visited, sizes)
    return sizes


def traverserNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    while nodesToExplore:
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        nodesToExplore += getUnvisitedNeighbors(i, j, matrix, visited)

    if currentRiverSize > 0:
        sizes.append(sizes)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])
    return unvisitedNeighbors
