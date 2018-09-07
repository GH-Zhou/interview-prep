import unittest

# ---- Assumptions
#      1. The words are separated by spaces only.
#      2. There's no leading or trailing spaces.
#      3. There is exactly one space between words.

# ---- Test Cases
#   1) Input: "",                   Output: ""
#   2) Input: "Hello",              Output: "Hello"
#   3) Input: "Hello World",        Output: "World Hello"
#   4) Input: "ab bc cd de",        Output: "de cd bc ab"
#   5) Input: "+ 1c 4d ga kyvr",    Output: "kyvr ga 4d 1c +"

# ---- Approach 1
# Idea: Split the input string into words_array, use slice to convert the array to its reversed form,
#       and finally join it back to a string using spaces.
#
# Implementation:
def reverse_words_1(str):
    words_array = str.split(" ")
    return " ".join(words_array[::-1])
# ---- Complexity
#   Time:  O(n), where n is the length of str
#   Space: O(n), spent on words_array and slicing


# ---- Approach 2
# Idea: Split the input string into words_array, use slice to convert the array to its reversed form,
#       and finally join it back to a string using spaces.
#
# Implementation:
def reverse_words_2(str):
    words_array = str.split(" ")
    start, end = 0, len(words_array) - 1
    while start < end:
        words_array[start], words_array[end] = words_array[end], words_array[start]
        start += 1
        end -= 1
    return " ".join(words_array)
# ---- Complexity
#   Time:  O(n), where n is the length of str
#   Space: O(n), spent on words_array


# ---- Approach 3 (Without words_array)
# Idea: reverse each word in its place, and finally reverse the whole string.
#
# Implementation:
def reverse_words_3(str):
    char_arr = list(str)
    w_left, w_right = 0, 0

    while w_left < len(char_arr) and w_right < len(char_arr):
        if char_arr[w_right] == " ":
            # reverse each word
            reverse(char_arr, w_left, w_right - 1)
            w_left = w_right + 1
        w_right += 1
    # reverse last word
    reverse(char_arr, w_left, w_right - 1)

    # reverse the whole string
    reverse(char_arr, 0, len(char_arr) - 1)
    return "".join(char_arr)

def reverse(char_arr, start, end):
    while start < end:
        char_arr[start], char_arr[end] = char_arr[end], char_arr[start]
        start += 1
        end -= 1

# ---- Complexity
#   Time:  O(n), where n is the length of str
#   Space: O(n), spent on generating char array and string only, other operations cost O(1) only

class TestReverseString(unittest.TestCase):

    def test_reverse_string_1(self):
        self.assertEqual(reverse_words_1(""), "")
        self.assertEqual(reverse_words_1("Hello"), "Hello")
        self.assertEqual(reverse_words_1("Hello World"), "World Hello")
        self.assertEqual(reverse_words_1("ab bc cd de"), "de cd bc ab")
        self.assertEqual(reverse_words_1("+ 1c 4d ga kyvr"), "kyvr ga 4d 1c +")

    def test_reverse_string_2(self):
        self.assertEqual(reverse_words_2(""), "")
        self.assertEqual(reverse_words_2("Hello"), "Hello")
        self.assertEqual(reverse_words_2("Hello World"), "World Hello")
        self.assertEqual(reverse_words_2("ab bc cd de"), "de cd bc ab")
        self.assertEqual(reverse_words_2("+ 1c 4d ga kyvr"), "kyvr ga 4d 1c +")

    def test_reverse_string_3(self):
        self.assertEqual(reverse_words_3(""), "")
        self.assertEqual(reverse_words_3("Hello"), "Hello")
        self.assertEqual(reverse_words_3("Hello World"), "World Hello")
        self.assertEqual(reverse_words_3("ab bc cd de"), "de cd bc ab")
        self.assertEqual(reverse_words_3("+ 1c 4d ga kyvr"), "kyvr ga 4d 1c +")