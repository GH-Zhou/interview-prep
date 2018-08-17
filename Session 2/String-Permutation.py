import unittest

# ---- Assumptions
#      The input will contain English letters only

# ---- Test Cases
#   1) Input: ""          Output: []
#   2) Input: "a"         Output: ["a", "A"]
#   3) Input: "ab"        Output: ["a", "ab", "aB", "A", "Ab", "AB", "b", "B"]
#   4) Input: "aB"        Output: ["a", "ab", "aB", "A", "Ab", "AB", "b", "B"]
#   5) Input: "AB"        Output: ["a", "ab", "aB", "A", "Ab", "AB", "b", "B"]
#   6) Input: "Ab"        Output: ["a", "ab", "aB", "A", "Ab", "AB", "b", "B"]
#   7) Input: "abc"       Output: ["a", "ab", "abc", "abC", "aB", "aBc", "aBC", "ac",
#                                  "aC", "A", "Ab", "Abc", "AbC", "AB", "ABc", "ABC", "Ac",
#                                  "AC", "b", "bc", "bC", "B", "Bc", "BC", "c", "C"]

# ---- Approach
# Idea: Use DFS to record each permutation
#
# Implementation:
class StringPermulation():
    def string_permutations_1(self, string):
        res = []
        if string == "":
            return res
        self.backtracking(string, res, 0, [])
        return res

    def backtracking(self, string, res, index, cur_str):
        if index > len(string):
            return

        if len(cur_str) > 0:
            res.append("".join(cur_str)[:])

        for i in range(index, len(string)):
            index += 1

            cur_str.append(string[i].lower())
            self.backtracking(string, res, index, cur_str)
            cur_str.pop()

            cur_str.append(string[i].upper())
            self.backtracking(string, res, index, cur_str)
            cur_str.pop()


# - Complexity
#   Observation from Test Case 3: 4 permutations for "ab", 2 for "a" and "b" respectively
#                    Test Case 7: 8 permutations for "abc", 4 for "ab", "ac", and "bc" respectively,
#                                 2 for "a", "b" and "c" respectively
#      Each permutation is 2 ^ k, where k is the length of this string;
#                                                   / n \     n(n - 1)...(n - k + 1)
#      The number of k-letter combination would be |     | = ------------------------, select k from n;
#                                                   \ k /         k(k - 1)...1
#      Each construction of a new string combination takes O(1);
#      As a result, the final time complexity would be:
#              n
#             ---     / n \
#   Time: O(  \    k |     | ) , where n is the length of the input string
#             /   2   \ k /
#             ---
#            k = 1
#
#   Extra Space: O(n), spent on stack memory

class TestStringPermutations(unittest.TestCase):
    def test_string_permutations(self):
        sp = StringPermulation()
        self.assertEqual(sp.string_permutations_1(""), [])
        self.assertEqual(sp.string_permutations_1("a"), ["a", "A"])
        self.assertEqual(sp.string_permutations_1("ab"), ["a", "ab", "aB", "A", "Ab", "AB", "b", "B"])
        self.assertEqual(sp.string_permutations_1("aB"), ["a", "ab", "aB", "A", "Ab", "AB", "b", "B"])
        self.assertEqual(sp.string_permutations_1("AB"), ["a", "ab", "aB", "A", "Ab", "AB", "b", "B"])
        self.assertEqual(sp.string_permutations_1("Ab"), ["a", "ab", "aB", "A", "Ab", "AB", "b", "B"])
        self.assertEqual(sp.string_permutations_1("abc"), ["a", "ab", "abc", "abC", "aB", "aBc", "aBC", "ac",
                                                        "aC", "A", "Ab", "Abc", "AbC", "AB", "ABc", "ABC", "Ac",
                                                        "AC", "b", "bc", "bC", "B", "Bc", "BC", "c", "C"])

if __name__ == '__main__':
    unittest.main()