"""[summary].
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


def staircaseTraversalHelper(height, maxSteps, memorize):
    if height in memorize:
        return memorize[height]
    else:
        numberOfWays = 0
        for step in range(1, min(maxSteps, height) + 1):
            numberOfWays += staircaseTraversalHelper(height - step, maxSteps,
                                                     memorize)
        memorize[height] = numberOfWays
        return numberOfWays


def staircaseTraversal(height, maxSteps):

    return staircaseTraversalHelper(height, maxSteps, memorize={0: 1, 1: 1})


def test1():
    height = 4
    steps = 2
    assert staircaseTraversal(height, steps) == 5


if __name__ == "__main__":
    test1()