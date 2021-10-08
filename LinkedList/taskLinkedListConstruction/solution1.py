"""
DoublyLinkedList class that has a head and a tail, both of which point to either a linked list Node or None / null. The class should
  
  support:

    Setting the head and tail of the linked list.
    Inserting nodes before and after other nodes as well as at given positions
    (the position of the head node is 1).
    Removing given nodes and removing nodes with given values.
    Searching for nodes with given values.

  Note that the setHead, setTail, insertBefore, insertAfter, insertAtPosition, and remove methods all take in
  actual Nodes as input parameters—not integers (except for  insertAtPosition, which also takes in an integer 
  representing the position); this means that you don't need to create any new Nodes
  in these methods. The input nodes can be either stand-alone nodes or nodes
  that are already in the linked list. If they're nodes that are already in the
  linked list, the methods will effectively be <i>moving</i> the nodes within
  the linked list. You won't be told if the input nodes are already in the
  linked list, so your code will have to defensively handle this scenario.
  If you're doing this problem in an untyped language like Python or JavaScript,
  you may want to look at the various function signatures in a typed language
  like Java or TypeScript to get a better idea of what each input parameter is.

  Each Node has an integer value as well as a prev node and a next node, both of which can point
  to either another node or None / null.

Sample Usage
// Assume the following linked list has already been created:
1 <-> 2 <-> 3 <-> 4 <-> 5
// Assume that we also have the following stand-alone nodes:
3, 3, 6
setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 // set the existing node with value 4 as the head
setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the stand-alone node with value 6 as the tail
insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the existing node with value 3 before the existing node with value 6
insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 after the existing node with value 6
insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 in position 1
removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all nodes with value 3
remove(2): 4 <-> 1 <-> 5 <-> 6 // remove the existing node with value 2
containsNodeWithValue(5): true

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #Time: O(1), Space: O(1)
    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.tail = node
            self.head = node
        else:
            self.insertBefore(self.head, node)

    # Time O(1), Space O(1)
    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    # Time: O(1), Space: O(1)
    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if not (nodeToInsert == self.head and nodeToInsert == self.tail):
            self.remove(nodeToInsert)
            nodeToInsert.prev = node.prev
            nodeToInsert.next = node
            if node.prev is None:
                self.head = nodeToInsert
            else:
                node.prev.next = nodeToInsert
            node.prev = nodeToInsert

    # Time: O(1), Space: O(1)
    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if not (nodeToInsert == self.head and nodeToInsert == self.tail):
            self.remove(nodeToInsert)
            nodeToInsert.prev = node
            nodeToInsert.next = node.next
            if node.next is None:
                self.tail = nodeToInsert
            else:
                node.next.prev = nodeToInsert
            node.next = nodeToInsert

    # Time: O(N), Space: O(1)
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
        else:
            node = self.head
            currentPosition = 1
            while node and position != currentPosition:
                currentPosition += 1
                node = node.next
            if node:
                self.insertBefore(node, nodeToInsert)
            else:
                self.setTail(nodeToInsert)

    # Time: O(N), Space: O(1)
    def removeNodesWithValue(self, value):
        # Write your code here.
        node = self.head
        while node:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # Time: O(1), Space: O(1)
    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def removeNodeBindings(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    # Time: O(n), Space: O(1)
    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
        while node and node.value != value:
            node = node.next
        return node is not None


def getNodeValuesTailToHead(linkedList):
    current = linkedList.tail
    nodeValues = []
    while current:
        nodeValues.append(current.value)
        current = current.prev
    return nodeValues


def getNodeValuesHeadToTail(linkedList):
    current = linkedList.head
    nodeValues = []
    while current:
        nodeValues.append(current.value)
        current = current.next
    return nodeValues


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne


def test1():
    linkedList = DoublyLinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    three2 = Node(3)
    three3 = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    bindNodes(one, two)
    bindNodes(two, three)
    bindNodes(three, four)
    bindNodes(four, five)
    linkedList.head = one
    linkedList.tail = five

    linkedList.setHead(four)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 3, 5]
    assert getNodeValuesTailToHead(linkedList) == [5, 3, 2, 1, 4]
    linkedList.remove(four)


def test2():
    linkedList = DoublyLinkedList()
    linkedList.setHead(Node(5))
    linkedList.setHead(Node(4))
    linkedList.setHead(Node(3))
    linkedList.setHead(Node(2))
    linkedList.setHead(Node(1))
    linkedList.setHead(Node(4))
    linkedList.setTail(Node(6))
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 3, 4, 5, 6]
    linkedList.insertBefore(Node(6), Node(3))
    linkedList.insertAfter(Node(6), Node(3))
    linkedList.insertAfter(Node(6), Node(3))
    linkedList.insertAtPosition(1, Node(3))
    linkedList.removeNodesWithValue(3)
    linkedList.remove(Node(2))
    linkedList.containsNodeWithValue(5)


if __name__ == "__main__":
    test1()
    test2()