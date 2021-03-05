"""You're given three inputs, all of which are instances of a class which has a 'name' 
property and an 'ancestor' property pointing to the node's immediate ancestor. 
The first input is the top ancestor in an ancestral tree (the only node that does not have an ancestor of its own), 
and the other two inputs are descendants in the ancestral tree. 
Write a function that returns the youngest common ancestor to the two descendents.

            A
          /   \
         B     C
       /   \  /  \ 
      D    E F    G
    /  \ 
   H    I

getYoungestCommonAncestor(Node A, Node E, Node H) <----- Should return Node B
"""


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    levelDescendantOne = getDescendantDepth(descendantOne, topAncestor)
    levelDescendantTwo = getDescendantDepth(descendantTwo, topAncestor)

    if levelDescendantOne < levelDescendantTwo:
        return backtrackToAncestral(descendantTwo, descendantOne,
                                    levelDescendantTwo - levelDescendantOne)
    else:
        return backtrackToAncestral(descendantOne, descendantTwo,
                                    levelDescendantOne - levelDescendantTwo)


def backtrackToAncestral(lowerDescendant, highDescendant, deptDiff):
    while deptDiff > 0:
        lowerDescendant = lowerDescendant.ancestor
        deptDiff -= 1
    while lowerDescendant != highDescendant:
        lowerDescendant = lowerDescendant.ancestor
        highDescendant = highDescendant.ancestor
    return lowerDescendant


def getDescendantDepth(descendant, ancestor):
    dept = 0
    while descendant != ancestor:
        dept += 1
        descendant = descendant.ancestor
    return dept


def getLevelOfNode(node):
    currentNode = node.ancestor
    levelNone = 0
    while currentNode:
        levelNone += 1
        currentNode = currentNode.ancestor
    return levelNone


class AncestralTree(AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


def test1():
    trees = new_trees()
    trees["A"].addDescendants(trees["B"], trees["C"])
    trees["B"].addDescendants(trees["D"], trees["E"])
    trees["D"].addDescendants(trees["H"], trees["I"])
    trees["C"].addDescendants(trees["F"], trees["G"])
    yca = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
    yca == trees["B"]


if __name__ == "__main__":
    test1()
