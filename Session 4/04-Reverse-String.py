import unittest

# ---- Test Cases
#   1) Input: "",                   Output: ""
#   2) Input: "a",                  Output: "a"
#   3) Input: "abcd",               Output: "dcba"
#   4) Input: "a b c d",            Output: "d c b a"
#   5) Input: " + 1c 4d ga kyvr",    Output: "rvyk ag d4 c1 + "

# ---- Approach 1
# Idea: Use slice to directly convert a string to its reversed form.
#
# Implementation:
def reverse_string_1(str):
    return str[::-1]
# ---- Complexity
#   Time:  O(n), where n is the length of str
#   Space: O(n), spent on slicing


# ---- Approach 2
# Idea: Initialize an empty string, and iterate the input string from end to start, append the character
#       to the new string during each iteration.
#
# Implementation:
def reverse_string_2(str):
    res_str = ""
    for i in reversed(range(len(str))):
        res_str += str[i]
    return res_str

# ---- Complexity
#   Time:  O(n^2), in each iteration, string concatenation will result in O(n) time
#   Space: O(n^2), in each iteration, string concatenation will result in O(n) extra space


# ---- Approach 3
# Idea: Use two pointers in a char array, beginning from start and end respectively,
#       swap them, and then move inward until they meet at midpoint.
#
# Implementation:
def reverse_string_3(str):
    char_arr = list(str)
    start, end = 0, len(char_arr) - 1
    while start < end:
        char_arr[start], char_arr[end] = char_arr[end], char_arr[start]
        start += 1
        end -= 1
    return "".join(char_arr)

# ---- Complexity
#   Time:  O(n), where n is the length of str
#   Space: O(n), spent on generating the char array


class TestReverseString(unittest.TestCase):

    def test_reverse_string_1(self):
        self.assertEqual(reverse_string_1(""), "")
        self.assertEqual(reverse_string_1("a"), "a")
        self.assertEqual(reverse_string_1("abcd"), "dcba")
        self.assertEqual(reverse_string_1("a b c d"), "d c b a")
        self.assertEqual(reverse_string_1(" + 1c 4d ga kyvr"), "rvyk ag d4 c1 + ")

    def test_reverse_string_2(self):
        self.assertEqual(reverse_string_2(""), "")
        self.assertEqual(reverse_string_2("a"), "a")
        self.assertEqual(reverse_string_2("abcd"), "dcba")
        self.assertEqual(reverse_string_2("a b c d"), "d c b a")
        self.assertEqual(reverse_string_2(" + 1c 4d ga kyvr"), "rvyk ag d4 c1 + ")

    def test_reverse_string_3(self):
        self.assertEqual(reverse_string_3(""), "")
        self.assertEqual(reverse_string_3("a"), "a")
        self.assertEqual(reverse_string_3("abcd"), "dcba")
        self.assertEqual(reverse_string_3("a b c d"), "d c b a")
        self.assertEqual(reverse_string_3(" + 1c 4d ga kyvr"), "rvyk ag d4 c1 + ")