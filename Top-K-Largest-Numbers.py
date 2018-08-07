import unittest
# ---- Assumptions
#   1) Array is not sorted;
#   2) the returned array is is any order;
#   3) if the input is invalid, return []

# ---- Test Cases
#   1) Input: [], K = 1,                                Output: []
#   2) Input: [1], K = 1,                               Output: [1]
#   3) Input: [2, 1], K = 1,                            Output: [2]
#   4) Input: [5, 1, 2, 9, 1], K = 3,                   Output: [5, 9, 2]
#   5) Input: [-1, -9, 3, 2, 8, 4, 2], K = 5,           Output: [3, 2, 8, 4, 2]

# ---- Approach 1 (Sort)
# Idea: Sort the array first and then return the slice of last K elements
# Implementation:
def top_k_largest_numbers_1(arr, K):
    # If the length of array is less than K, it's an invalid input, return an empty array
    if len(arr) < K: return []

    arr.sort()
    return arr[-K:]

# - Complexity
#   Time:  O(n logn), spent on sorting the array
#   Space: O(n), spent on built-in method sort()


# ---- Approach 2 (Quick Select)
# Idea: Using Quick Select to find the Kth largest number, when the Kth largest number is found,
#       the slice of first K elements will be the top K largest numbers
# Implementation:
def top_k_largest_numbers_2(arr, K):
    if len(arr) < K: return []

    index = quickSelect(arr, 0, len(arr) - 1, K - 1)
    return arr[:(index+1)]

def quickSelect(arr, start, end, K):
    # Exit of recursion: return the index if two pointers collide
    if start == end: return start
    i, j = start, end
    pivot = arr[(i + j) // 2]

    # Move all the elements larger than pivot to the left, and those smaller than it to the right
    while i <= j:
        while i <= j and arr[i] > pivot: i += 1
        while i <= j and arr[j] < pivot: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if K <= j: # len(arr[:j]) is larger than or equal to K, thus continue searching in the left part
        return quickSelect(arr, start, j, K)
    if K >= i: # len(arr[:i]) is less than or equal to K, thus continue searching in the right part
        return quickSelect(arr, i, end, K)
    return K
# - Complexity:
#   Time:  Amortized O(n), Worst case O(n^2)
#   Space: Worst case O(n), spent on recursion using stack memory

# ---- Trade off
#       While the 2nd approach has a amortized time complexity of O(n), sometimes it may result in O(n^2)
#   due to certain kinds of input.
#       If a system is emphasizing the stability of running time, I'd use the built-in sort function to
#   find the k largest numbers. In Python, sort() implements Timsort, which is a stable sorting algorithm
#   with the worst time complexity of O(n logn) and space complexity of O(n).
#       If a system is not caring about that, Quick Select would definitely be a better solution since it
#   has an amortized running time of O(n), which would suffice for most of cases

# ---- Unit Test
class TestTopKLargestNumbers(unittest.TestCase):
    arr1 = []
    arr2 = [1]
    arr3 = [2, 1]
    arr4 = [5, 1, 2, 9, 1]
    arr5 = [-1, -9, 3, 2, 8, 4, 2]

    def test_top_k_largest_numbers_1(self):
        self.assertEqual(top_k_largest_numbers_1(self.arr1, 1), [])
        self.assertEqual(top_k_largest_numbers_1(self.arr2, 1), [1])
        self.assertEqual(top_k_largest_numbers_1(self.arr3, 1), [2])
        self.assertEqual(top_k_largest_numbers_1(self.arr4, 3), [2, 5, 9])
        self.assertEqual(top_k_largest_numbers_1(self.arr5, 5), [2, 2, 3, 4, 8])

    def test_top_k_largest_numbers_2(self):
        self.assertEqual(top_k_largest_numbers_2(self.arr1, 1), [])
        self.assertEqual(top_k_largest_numbers_2(self.arr2, 1), [1])
        self.assertEqual(top_k_largest_numbers_2(self.arr3, 1), [2])
        self.assertEqual(top_k_largest_numbers_2(self.arr4, 3), [9, 5, 2])
        self.assertEqual(top_k_largest_numbers_2(self.arr5, 5), [8, 4, 3, 2, 2])

if __name__ == '__main__':
    unittest.main()