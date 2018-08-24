import unittest

# ---- Test Cases
#   1) Input: [], 1                                            Output: False
#   2) Input: [3, 2, 1, 6], 9                                  Output: True
#   3) Input: [-5, 5, 2, 4], -1                                Output: True
#   4) Input: [5, 4, 2, 1], 1                                  Output: False
#   5) Input: [-1, 1, 3, -5, 7, -9], 11                        Output: False

# ---- Approach 1
# Idea: Sort the given array and use two pointers (start and end) to find the target
#
# Implementation:
def two_sum_1(array, target):
    if len(array) < 2:
        return False
    array.sort()
    start, end = 0, len(array) - 1
    while start < end:
        if array[start] + array[end] == target:
            return True
        elif array[start] + array[end] < target:
            start += 1
        else:
            end -= 1
    return False
# - Complexity
#   Time: O(n log(n)), spent on sorting input array
#   Space: O(n), spent on sorting the array

# ---- Approach 1
# Idea: Use a hashSet to record the visited number, and return True if target MINUS current number exists
#       in the set
#
# Implementation:
def two_sum_2(array, target):
    if len(array) < 2:
        return False
    visited = set([])
    for num in array:
        if target - num in visited:
            return True
        visited.add(num)
    return False
# - Complexity
#   Time: O(n), spent on iterating the array
#   Space: O(n), spent on caching the visited number

# ---- Trade-off
#   While the first approach is using constant space complexity during iterating the array; however, during
#   sorting, it will consume O(n) space. Thus the overall space complexity would still be O(n). The second
#   approach uses a hash table to record what have been seen in the past iterations, which enables O(1) access
#   to the previous visited number.

class TestTwoSum(unittest.TestCase):
    array1 = []
    array2 = [3, 2, 1, 6]
    array3 = [-5, 5, 2, 4]
    array4 = [5, 4, 2, 1]
    array5 = [-1, 1, 3, -5, 7, -9]

    def test_two_sum_1(self):
        self.assertFalse(two_sum_1(self.array1, 1))
        self.assertTrue(two_sum_1(self.array2, 9))
        self.assertTrue(two_sum_1(self.array3, -1))
        self.assertFalse(two_sum_1(self.array4, 1))
        self.assertFalse(two_sum_1(self.array5, 11))

    def test_two_sum_2(self):
        self.assertFalse(two_sum_2(self.array1, 1))
        self.assertTrue(two_sum_2(self.array2, 9))
        self.assertTrue(two_sum_2(self.array3, -1))
        self.assertFalse(two_sum_2(self.array4, 1))
        self.assertFalse(two_sum_2(self.array5, 11))