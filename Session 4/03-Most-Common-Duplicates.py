import unittest, collections

# ---- Assumptions
#      You may assume there's a unique answer

# ---- Test Cases
#   1) Input: [1],       Output: 1
#   2) Input: [1, 1],    Output: 1
#   3) Input: [1, 2, 2], Output: 2
#   4) Input: [1, 2, 2, 4, 4, 4], Output: 4
#   5) Input: [1, 2, 2, 3, 3, 3, 4, 4], Output: 3

# ---- Approach 1 (Dictionary)
# Idea: Use a dictionary to record the count of each element and find the key with maximum value.
#
# Implementation:
def most_common_duplicates_1(arr):
    if len(arr) == 1:
        return arr[0]
    c = collections.Counter(arr)
    max_key, max_value = None, 1
    for key, value in c.items():
        if max_value < value:
            max_value = value
            max_key = key
    return max_key
# ---- Complexity
#   Time:  O(n), where n is the length of arr
#   Space: O(n), where the worst case is that all the elements are not equal except two elements

# ---- Approach 2 (Constant Space)
# Idea: Simply iterate the array and keep a count variable to record the most common duplicates
#
# Implementation:

def most_common_duplicates_2(arr):
    if len(arr) == 1:
        return arr[0]
    max_count, cur_count, i = 1, 1, 1
    most_common = None

    while i < len(arr):
        # if current element equals to the last one, increment cur_count by one
        if arr[i - 1] == arr[i]:
            cur_count += 1
        # else, if cur_count is greater than max_count, update most_common element and max_count
        elif cur_count > max_count:
            most_common = arr[i - 1]
            max_count = cur_count
            cur_count = 1
        i += 1

    # double check the last element
    if cur_count > max_count:
        most_common = arr[i - 1]
    return most_common
# ---- Complexity
#   Time:  O(n), where n is the length of arr
#   Space: O(1)

class TestMostCommonDuplicates(unittest.TestCase):

    def test_most_common_duplicates_1(self):
        self.assertEqual(most_common_duplicates_1([1]), 1)
        self.assertEqual(most_common_duplicates_1([1, 1]), 1)
        self.assertEqual(most_common_duplicates_1([1, 2, 2]), 2)
        self.assertEqual(most_common_duplicates_1([1, 2, 2, 4, 4, 4]), 4)
        self.assertEqual(most_common_duplicates_1([1, 2, 2, 3, 3, 3, 4, 4]), 3)

    def test_most_common_duplicates_2(self):
        self.assertEqual(most_common_duplicates_2([1]), 1)
        self.assertEqual(most_common_duplicates_2([1, 1]), 1)
        self.assertEqual(most_common_duplicates_2([1, 2, 2]), 2)
        self.assertEqual(most_common_duplicates_2([1, 2, 2, 4, 4, 4]), 4)
        self.assertEqual(most_common_duplicates_2([1, 2, 2, 3, 3, 3, 4, 4]), 3)
