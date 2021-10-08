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


# Time: O(N), Space O(1)
def findSubstring(s, k):
    # Write your code here
    subStr = "Not found!"
    isVowel = lambda x: x in "aeiou"
    vowCounter = len(list(filter(isVowel, s[:k])))
    maxVowel = 0
    if maxVowel < vowCounter:
        maxVowel = vowCounter
        subStr = s[:k]
    for idx in range(k - 1, len(s)):
        vowCounter += 1 if isVowel(s[idx]) else 0
        vowCounter -= 1 if isVowel(s[idx - k]) else 0
        if maxVowel < vowCounter:
            maxVowel = vowCounter
            subStr = s[idx - k:idx]
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