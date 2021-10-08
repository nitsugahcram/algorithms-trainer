"""[summary].
  You're given two positive integers representing the height of a staircase and
  the maximum number of steps that you can advance up the staircase at a time.
  Write a function that returns the number of ways in which you can climb the
  staircase.
  For example, if you were given a staircase of height = 3 and
  maxSteps = 2 you could climb the staircase in 3 ways. You could
  take 1 step, 1 step, then 1 step</b>, you could also take
  1 step, then 2 steps</b>, and you could take 2 steps, then 1 step</b>.

Note that maxSteps &lt;= height will always be true.
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


def staircaseTraversal(height, maxSteps):
    currentNumberOfWays = 0
    waysToTop = [1]

    for currentHeight in range(1, height + 1):
        startWindow = currentHeight - maxSteps - 1
        endWindow = currentHeight - 1
        if startWindow >= 0:
            currentNumberOfWays -= waysToTop[startWindow]
        currentNumberOfWays += waysToTop[endWindow]
        waysToTop.append(currentHeight)
    return waysToTop[height]