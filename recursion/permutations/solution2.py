"""
  Write a function that takes in an array of unique integers and returns an
  array of all permutations of those integers in no particular order.

If the input array is empty, the function should return an empty array.
Sample Input
array = [1, 2, 3]

Sample Output
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""


def permutationHelper(i, array, permutations):

    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationHelper(i + 1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def getPermutations(array):
    # Write your code here.
    permutations = []
    permutationHelper(0, array, permutations)
    return permutations