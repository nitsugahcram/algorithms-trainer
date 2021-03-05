"""You are given a circular array nums of positive and negative integers. 
If a number k at an index is positive, then move forward k steps. Conversely, 
if it's negative (-k), move backward k steps. Since the array is circular,
 you may assume that the last element's next element is the first element, 
 and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. 
A cycle must start and end at the same index and the cycle's length > 1. Furthermore, 
movements in a cycle must all follow a single direction. 
In other words, a cycle must not consist of both forward and backward movements.

Cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index sequence 
* seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
* Every nums[seq[j]] is either all positive or all negative.
* k > 1

"""


# Time: O(n)
# Space: O(n)
def hasSingleCycle1(array):
    # Write your code here.
    lenArr = len(array)
    nextIdx = 0
    hasIndex = []
    count = 0
    while count < lenArr:
        target = array[nextIdx]
        nextIdx = ((target % lenArr) + nextIdx) % lenArr
        if nextIdx in hasIndex:
            break
        hasIndex.append(nextIdx)
        count += 1
    return count == lenArr


def getNextIdx(currentIdx, jump, lenArr):
    nextIdx = (jump + currentIdx) % lenArr
    return nextIdx if nextIdx >= 0 else nextIdx + lenArr


#Time: O(N), Space: O(1)
def hasSingleCycle(array):
    lenArr = len(array)
    currentIdx = 0
    numberOfVisit = 0
    while numberOfVisit < lenArr:
        if currentIdx == 0 and numberOfVisit > 0:
            return False
        currentIdx = getNextIdx(currentIdx, array[currentIdx], lenArr)
        numberOfVisit += 1

    return currentIdx == 0


def test13():
    arr = [2, 3, 1, -4, -4, 2]
    hasSingleCycle(arr)
    pass


def test1():
    arr = [1, -1, 1, -1]
    hasSingleCycle(arr)
    pass


def test2():
    arr = [10, 11, -6, -23, -2, 3, 88, 909, -26]
    hasSingleCycle(arr)


if __name__ == '__main__':
    test2()