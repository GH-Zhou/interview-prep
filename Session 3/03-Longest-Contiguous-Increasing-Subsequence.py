import unittest

# ---- Test Cases
#   1) Input: []                              Output: 0
#   2) Input: [1]                             Output: 1
#   3) Input: [1, 1]                          Output: 1
#   4) Input: [1, 2, 2, 3]                    Output: 2
#   5) Input: [-1, 2, 3, 5, 9, 3]             Output: 5

# ---- Approach
# Idea: Simply iterate through the array and keep the current length and compare it with the longest contiguous
#       increasing subsequence
#
# Implementation:
def longest_contiguous_increasing_subsequence(array):
    if len(array) < 2: return len(array)
    maxLength = 1
    i = 0
    while i < len(array) - 1:
        curLength = 1
        while i < len(array) - 1 and array[i] < array[i + 1]:
            curLength += 1
            i += 1
        i += 1
        maxLength = max(maxLength, curLength)
    return maxLength
# - Complexity
#   Time: O(n), spent on iterating the array
#   Space: O(1)

class TestLongestContiguousIncreasingSubsequence(unittest.TestCase):
    array1 = []
    array2 = [1]
    array3 = [1, 1]
    array4 = [1, 2, 2, 3]
    array5 = [-1, 2, 3, 5, 9, 3]

    def test_longest_contiguous_increasing_subsequence(self):
        self.assertEqual(longest_contiguous_increasing_subsequence(self.array1), 0)
        self.assertEqual(longest_contiguous_increasing_subsequence(self.array2), 1)
        self.assertEqual(longest_contiguous_increasing_subsequence(self.array3), 1)
        self.assertEqual(longest_contiguous_increasing_subsequence(self.array4), 2)
        self.assertEqual(longest_contiguous_increasing_subsequence(self.array5), 5)
