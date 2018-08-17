import unittest

# To keep it simple, let's use 0, 1, and 2 to represent Red, White and Blue respectively
# ---- Test Cases
#   1) Input: []                        Output: []
#   2) Input: [0]                       Output: [0]
#   3) Input: [2, 0]                    Output: [0, 2]
#   4) Input: [1, 0, 2]                 Output: [0, 1, 2]
#   5) Input: [1, 0, 1, 0]              Output: [0, 0, 1, 1]
#   6) Input: [1, 2, 1, 0]              Output: [0, 1, 1, 2]
#   7) Input: [0, 2, 1, 0, 2]           Output: [0, 0, 1, 2, 2]
#   8) Input: [2, 0, 1, 2, 1, 0]        Output: [0, 0, 1, 1, 2, 2]
#   9) Input: [2, 2, 2, 2, 1, 1, 0, 0]  Output: [0, 0, 1, 1, 2, 2, 2, 2]

# ---- Approach 1
# Idea: Similar to counting sort, count the colors first and arrange the colors using the counts.
#
# Implementation:
def sort_colors_1(colors):
    counts = [0, 0, 0]
    for color in colors:
        counts[color] += 1
    i = 0
    for color, cnt in enumerate(counts):
        while cnt > 0:
            colors[i] = color
            i += 1
            cnt -= 1
    return colors
# - Complexity
#   Time: O(n), where n is the length of colors array, two passes
#   Space: O(1) for three colors

# ---- Approach 2
# Idea: Use three pointers to keep track of cur_index, red_index and blue_index respectively
#
# Implementation:
def sort_colors_2(colors):
    cur_index, red_index, blue_index = 0, 0, len(colors) - 1
    while cur_index <= blue_index:
        if colors[cur_index] == 0:
            colors[cur_index] = colors[red_index]
            colors[red_index] = 0
            red_index += 1
        if colors[cur_index] == 2:
            colors[cur_index] = colors[blue_index]
            colors[blue_index] = 2
            blue_index -= 1
            cur_index -= 1  # need double check original color at blue_index before swap
        cur_index += 1
    return colors
# - Complexity
#   Time: O(n), where n is the length of colors array, one pass
#   Space: O(1)

# ---- Trade off
#   The two approaches share the same Time and Space Complexity.
#   While the first approach is more intuitive but it's a two-pass algorithm, and it also consumes an array
#   to store each color's count; the second approach only uses swaps, without counting the colors beforehand.

class TestSortColors(unittest.TestCase):
    def test_sort_colors_1(self):
        self.assertEqual(sort_colors_1([]), [])
        self.assertEqual(sort_colors_1([0]), [0])
        self.assertEqual(sort_colors_1([2, 0]), [0, 2])
        self.assertEqual(sort_colors_1([1, 0, 2]), [0, 1, 2])
        self.assertEqual(sort_colors_1([1, 0, 1, 0]), [0, 0, 1, 1])
        self.assertEqual(sort_colors_1([1, 2, 1, 0]), [0, 1, 1, 2])
        self.assertEqual(sort_colors_1([0, 2, 1, 0, 2]), [0, 0, 1, 2, 2])
        self.assertEqual(sort_colors_1([2, 0, 1, 2, 1, 0]), [0, 0, 1, 1, 2, 2])
        self.assertEqual(sort_colors_1([2, 2, 2, 2, 1, 1, 0, 0]), [0, 0, 1, 1, 2, 2, 2, 2])

    def test_sort_colors_2(self):
        self.assertEqual(sort_colors_2([]), [])
        self.assertEqual(sort_colors_2([0]), [0])
        self.assertEqual(sort_colors_2([2, 0]), [0, 2])
        self.assertEqual(sort_colors_2([1, 0, 2]), [0, 1, 2])
        self.assertEqual(sort_colors_2([1, 0, 1, 0]), [0, 0, 1, 1])
        self.assertEqual(sort_colors_2([1, 2, 1, 0]), [0, 1, 1, 2])
        self.assertEqual(sort_colors_2([0, 2, 1, 0, 2]), [0, 0, 1, 2, 2])
        self.assertEqual(sort_colors_2([2, 0, 1, 2, 1, 0]), [0, 0, 1, 1, 2, 2])
        self.assertEqual(sort_colors_2([2, 2, 2, 2, 1, 1, 0, 0]), [0, 0, 1, 1, 2, 2, 2, 2])

if __name__ == '__main__':
    unittest.main()