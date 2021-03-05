"""Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

It uses the opposite strategy of depth-first search, which instead explores the node branch as far as possible before being forced to backtrack and expand other nodes.[2]

BFS and its application in finding connected components of graphs were invented in 1945 by Konrad Zuse, in his (rejected) Ph.D. thesis on the Plankalkül programming language, but this was not published until 1972.[3] It was reinvented in 1959 by Edward F. Moore, who used it to find the shortest path out of a maze,[4][5] and later developed by C. Y. Lee into a wire routing algorithm (published 1961).[6]
"""
from queue import Queue


# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # TIme: O(v+e), Space: o(v)
    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = Queue()
        queue.put(self)
        while not queue.empty():
            currentNode = queue.get()
            for node in currentNode.children:
                queue.put(node)
            array.append(currentNode.name)
        return array

    # TIme: O(v+e), Space: o(v)
    def _readthFirstSearch(self, array):
        # Write your code here.
        queue = [self]
        while queue:
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            for node in currentNode.children:
                queue.append(node)
            array.append(currentNode.name)
        return array


if __name__ == "__main__":
    pass