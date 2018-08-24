import unittest

# ---- Definition of TreeNode Class
#      A TreeNode is a node in a binary tree with its value and left/right properties
#      pointing to the left/right children
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ---- Test Cases
#   1) Input:   7           , 1                Output: 3
#             /   \
#            3     9
#           / \   / \
#          1   5 8   10

#   2) Input:   7           , 3                Output: 5
#             /   \
#            3     9
#           / \   / \
#          1   5 8   10

#   3) Input:   7           , 5                Output: 7
#             /   \
#            3     9
#           / \   / \
#          1   5 8   10

#   4) Input:   7           , 7                Output: 8
#             /   \
#            3     9
#           / \   / \
#          1   5 8   10

#   5) Input:   7           , 10               Output: None
#             /   \
#            3     9
#           / \   / \
#          1   5 8   10

# ---- Approach 1
# Idea: In-order Traversal
#
# Implementation:
class Solution1():

    def next_larger_element_BST_1(self, root, pre):
        self.res = None
        self.last_val = None
        self.dfs(root, pre)
        return self.res

    def dfs(self, node, pre):
        if node is None:
            return

        self.dfs(node.left, pre)
        if self.last_val == pre.val:
            self.res = node
        self.last_val = node.val
        self.dfs(node.right, pre)

# - Complexity
#   Time: O(n), where n is the number of the nodes in the BST
#   Space: O(log(n)) if BST is balanced, spent on recursion stack memory

# ---- Approach 2 (Optimization On Time)
# Idea: Recursively search on the right subtree if the current value is less than predecessor's value
#       else search on the left subtree
#
# Implementation:
class Solution2():

    def next_larger_element_BST_2(self, root, pre):

        if root is None or pre is None: return None

        if root.val <= pre.val:
            return self.next_larger_element_BST_2(root.right, pre)
        else:
            left = self.next_larger_element_BST_2(root.left, pre)
            return left if left else root
# - Complexity
#   Time: O(log(n)), where n is the number of the nodes in the BST
#   Space: O(log(n)) if BST is balanced, spent on recursion stack memory

# ---- Why is the second approach much faster?
#   The second approach is much faster than the first one because each recursion it throws half of the
#   possible results based on the fact that the next larger element for the given predecessor cannot lie
#   in the subtree which is less than the predecessor.

class TestNextLargerElementBST(unittest.TestCase):
    sol1 = Solution1()
    sol2 = Solution2()
    t = TreeNode(7)
    t.left = TreeNode(3)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(5)
    t.right = TreeNode(9)
    t.right.left = TreeNode(8)
    t.right.right = TreeNode(10)

    def test_next_larger_element_bst_1(self):
        self.assertEqual(self.sol1.next_larger_element_BST_1(self.t, self.t.left.left), self.t.left)
        self.assertEqual(self.sol1.next_larger_element_BST_1(self.t, self.t.left), self.t.left.right)
        self.assertEqual(self.sol1.next_larger_element_BST_1(self.t, self.t.left.right), self.t)
        self.assertEqual(self.sol1.next_larger_element_BST_1(self.t, self.t), self.t.right.left)
        self.assertEqual(self.sol1.next_larger_element_BST_1(self.t, self.t.right.right), None)

    def test_next_larger_element_bst_2(self):
        self.assertEqual(self.sol2.next_larger_element_BST_2(self.t, self.t.left.left), self.t.left)
        self.assertEqual(self.sol2.next_larger_element_BST_2(self.t, self.t.left), self.t.left.right)
        self.assertEqual(self.sol2.next_larger_element_BST_2(self.t, self.t.left.right), self.t)
        self.assertEqual(self.sol2.next_larger_element_BST_2(self.t, self.t), self.t.right.left)
        self.assertEqual(self.sol2.next_larger_element_BST_2(self.t, self.t.right.right), None)
