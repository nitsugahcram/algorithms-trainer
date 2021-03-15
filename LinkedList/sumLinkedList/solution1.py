"""
  You're given two Linked Lists of potentially unequal length. Each Linked List
  represents a non-negative integer, where each node in the Linked List is a
  digit of that integer, and the first node in each Linked List always
  represents the least significant digit of the integer. Write a function that
  returns the head of a new Linked List that represents the sum of the integers
  represented by the two input Linked Lists.
  Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to
  None / null if it's the tail of the list. 
  The value of each LinkedList node is always in the range of 0 - 9.
  Note: your function must create and return a new Linked List, and you're not
  allowed to modify either of the input Linked Lists.

Sample Input
linkedListOne = 2 -&gt; 4 -&gt; 7 -&gt; 1
linkedListTwo = 9 -&gt; 4 -&gt; 5


<h3>Sample Output</h3>
1 -&gt; 9 -&gt; 2 -&gt; 2
// linkedListOne represents 1742
// linkedListTwo represents 549
// 1742 + 549 = 2291
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Time O(N) -> N is max (nl2, nl1)
# Space O(1)
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    dummy = LinkedList(0)
    current = dummy
    carryOn = 0
    while linkedListOne or linkedListTwo:
        valueOne = linkedListOne.value if linkedListOne else 0
        valueTwo = linkedListTwo.value if linkedListTwo else 0
        value = (valueOne + valueTwo) % 10 + carryOn
        carryOn = (valueOne + valueTwo) // 10
        current.next = LinkedList(value)
        current = current.next
        linkedListOne = linkedListOne.next if linkedListOne else None
        linkedListTwo = linkedListTwo.next if linkedListTwo else None

    if carryOn > 0:
        current.next = LinkedList(carryOn)
    return dummy.next