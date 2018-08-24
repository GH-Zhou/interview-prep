import unittest

# ---- Test Cases
#   1) Input: ""                             Output: 0
#   2) Input: "0"                            Output: 0
#   3) Input: "1"                            Output: 1
#   4) Input: "10"                           Output: 1
#   5) Input: "12"                           Output: 2
#   6) Input: "226"                          Output: 3

# ---- Approach 1
# Idea: Use dynamic programming to count the ways of decode
#
# Implementation:
def decode_ways(str):
    if str is None or len(str) == 0 or str[0] == "0": return 0
    dp = [0] * len(str)
    dp[0] = 1
    for i in range(1, len(str)):
        if str[i] == "0":
            if str[i - 1] == "1" or str[i - 1] == "2":
                dp[i] = dp[i - 2] if i > 1 else 1
            else:
                dp[i] = 0
        else:
            if "10" <= str[(i - 1):(i + 1)] <= "26":
                dp[i] = dp[i - 1] + dp[i - 2] if i > 1 else 2
            else:
                dp[i] = dp[i - 1]
    return dp[len(str) - 1]

# - Complexity
#   Time: O(n), spent on iterating the array
#   Space: O(n), spent on dp caching array

# ---- Approach 2 (Optimization on Space)
# Idea: Use a rolling array to minimize the use of caching memory
#
# Implementation:
def decode_ways_with_constant_space(str):
    n = len(str)
    if str is None or n == 0 or str[0] == "0": return 0
    dp = [1, 0]
    for i in range(1, n):
        if str[i] == "0":
            if str[i - 1] == "1" or str[i - 1] == "2":
                dp[i % 2] = dp[(i - 2) % 2] if i > 1 else 1
            else:
                dp[i % 2] = 0
        else:
            if "10" <= str[(i - 1):(i + 1)] <= "26":
                dp[i % 2] = dp[(i - 1) % 2] + dp[(i - 2) % 2] if i > 1 else 2
            else:
                dp[i % 2] = dp[(i - 1) % 2]
    return dp[(n - 1) % 2]

# - Complexity
#   Time: O(n), spent on iterating the array
#   Space: O(1)

class TestDecodeWays(unittest.TestCase):
    str1 = ""
    str2 = "0"
    str3 = "1"
    str4 = "10"
    str5 = "12"
    str6 = "226"

    def test_decode_ways(self):
        self.assertEqual(decode_ways(self.str1), 0)
        self.assertEqual(decode_ways(self.str2), 0)
        self.assertEqual(decode_ways(self.str3), 1)
        self.assertEqual(decode_ways(self.str4), 1)
        self.assertEqual(decode_ways(self.str5), 2)
        self.assertEqual(decode_ways(self.str6), 3)

    def test_decode_ways_with_constant_space(self):
        self.assertEqual(decode_ways_with_constant_space(self.str1), 0)
        self.assertEqual(decode_ways_with_constant_space(self.str2), 0)
        self.assertEqual(decode_ways_with_constant_space(self.str3), 1)
        self.assertEqual(decode_ways_with_constant_space(self.str4), 1)
        self.assertEqual(decode_ways_with_constant_space(self.str5), 2)
        self.assertEqual(decode_ways_with_constant_space(self.str6), 3)