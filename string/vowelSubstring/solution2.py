#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
Time: O(n^2), Space: 0(1)
def findSubstring(s, k):
    # Write your code here
    subStr = "Not found!"
    numVowel = 0
    lenStr = len(s)
    for startIdx in range(lenStr - k):
        currentVowel = 0
        for idx in range(startIdx, startIdx + k):
            if s[idx] in "aeiou":
                currentVowel += 1
        if currentVowel > numVowel:
            numVowel = currentVowel
            subStr = s[startIdx:startIdx + k]
        if numVowel == k:
            break
    return subStr


def test1():
    s = "qwdftr"
    k = 2
    assert findSubstring(s, k) == "Not found!"
    s = "eiuaooo"
    k = 4
    assert findSubstring(s, k) == "eiua"


if __name__ == "__main__":
    test1()