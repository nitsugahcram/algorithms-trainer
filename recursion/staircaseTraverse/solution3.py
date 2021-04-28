"""[Iteratitions].
  You're given two positive integers representing the height of a staircase and
  the maximum number of steps that you can advance up the staircase at a time.
  Write a function that returns the number of ways in which you can climb the
  staircase.
  For example, if you were given a staircase of height = 3 and
  maxSteps = 2 you could climb the staircase in 3 ways. You could
  take 1 step, 1 step, then 1 step, you could also take
  1 step, then 2 steps, and you could take 2 steps, then 1 step.

Note that maxSteps <= height will always be true.
Sample Input
    height = 4
    maxSteps = 2
Sample Output
    5
// You can climb the staircase in the following ways: 
    // 1, 1, 1, 1
    // 1, 1, 2
    // 1, 2, 1
    // 2, 1, 1
    // 2, 2
"""

# Time O(K*N) -> K (k the step allowed to make), N is Hight of Staircase
# Space O(N)


def staircaseTraversal(height, maxSteps):
    waysToStop = [0 for _ in range(height + 1)]
    waysToStop[0] = 1
    waysToStop[1] = 1

    currentHeight = 1
    for currentHeight in range(2, height + 1):
        step = 1
        while step <= maxSteps and step <= currentHeight:
            waysToStop[currentHeight] += currentHeight[currentHeight - step]
            step += 1

    return waysToStop[currentHeight]


def test1():
    height = 1
    maxStep = 1
    staircaseTraversal(height, maxStep) == 1


if __name__ == "__main__":
    test1()