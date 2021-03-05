"""Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

A version of depth-first search was investigated in the 19th century by French mathematician Charles Pierre Trémaux[1] as a strategy for solving mazes.[2][3]

              A
          /   |   \
         B    C    D
       /   \      /  \ 
      E    F     G    H
          /  \ 
         I    J

    depthFirstSearch() ->  ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

"""


# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Time: O(v + e), Space=O(v):
    # where v-> vertices
    # e -> Number of elements

    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
        for item in self.children:
            array = item.depthFirstSearch(array)
        return array