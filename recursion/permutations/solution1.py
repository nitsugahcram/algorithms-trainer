"""
  Write a function that takes in an array of unique integers and returns an
  array of all permutations of those integers in no particular order.

If the input array is empty, the function should return an empty array.
Sample Input
array = [1, 2, 3]

Sample Output
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""


def permutationHelper(array, currentPermutation, permutations):

    if not array and currentPermutation:
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutation + [array[i]]
            permutationHelper(newArray, newPermutation, permutations)


def getPermutations(array):
    # Write your code here.
    permutations = []
    permutationHelper(array, [], permutations)
    return permutations