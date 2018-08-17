import unittest
from collections import deque

# ---- Definition of TreeNode Class
#      A TreeNode is a node in a binary tree with its value and left/right properties
#      pointing to the left/right children
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ---- Test Cases
#   1) Input: None                     Output: []
#   2) Input:  1                       Output: [[1]]
#   3) Input:  1                       Output: [[1], [2, 3]]
#             / \
#            2   3
#   4) Input:  1                       Output: [[1],
#               \                               [3],
#                3                              [2, 4],
#               / \                             [5, 6, 7]]
#              2   4
#             /   / \
#            5   6   7

# ---- Approach 1
# Idea: Breadth-First Search
#
# Implementation:
def binary_tree_level_traversal_1(root):
    if root is None: return []
    q = deque([root])
    res = []
    while q:
        q_len = len(q)
        level = []
        for i in range(q_len):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level[:])
    return res
# - Complexity
#   Time: O(n), where n is the number of nodes in the binary tree
#   Space: O(2 ^ d), where d is the depth of the binary tree

# ---- Approach 2
# Idea: Depth-First Search (Modified Preorder Traversal: Root, Right, Left)
#
# Implementation:
def binary_tree_level_traversal_2(root):
    if root is None: return []
    level = 0
    stack = [(root, level)]
    res = []
    while stack:
        node, level = stack.pop()
        if level == len(res):
            res.append([node.val])
        else:
            res[level].append(node.val)
        if node.right: # Append right first to preserve the order of level traversal
            stack.append((node.right, level + 1))
        if node.left:
            stack.append((node.left, level + 1))
    return res
# - Complexity
#   Time: O(n), where n is the number of nodes in the binary tree
#   Space: O(d), where d is the depth of the binary tree

# ---- Trade off
#   Both of BFS and DFS approaches will visit each node once thus the time is O(n).
#   While BFS approach is more intuitive for the level traversal, it consumes more space in that it needs to
#   keep track of all the nodes at one level where the number of nodes can reach 2 ^ depth at most. And since
#   the depth equals to (log n) if the binary tree is balanced enough, 2 ^ depth actually has a complexity O(n)
#   For DFS, all you need to do is record the previous visited nodes along a path beginning from root. This is
#   an O(depth) space complexity.

class TestBinaryTreeLevelTraversal(unittest.TestCase):
    t1 = None

    t2 = TreeNode(1)

    t3 = TreeNode(1); t3.left = TreeNode(2); t3.right = TreeNode(3)

    t4 = TreeNode(1); t4.right = TreeNode(3); t4.right.left = TreeNode(2); t4.right.left.left = TreeNode(5)
    t4.right.right = TreeNode(4); t4.right.right.left = TreeNode(6); t4.right.right.right = TreeNode(7)

    def test_binary_tree_level_traversal_1(self):
        self.assertEqual(binary_tree_level_traversal_1(self.t1), [])
        self.assertEqual(binary_tree_level_traversal_1(self.t2), [[1]])
        self.assertEqual(binary_tree_level_traversal_1(self.t3), [[1], [2, 3]])
        self.assertEqual(binary_tree_level_traversal_1(self.t4), [[1], [3], [2, 4], [5, 6, 7]])

    def test_binary_tree_level_traversal_2(self):
        self.assertEqual(binary_tree_level_traversal_2(self.t1), [])
        self.assertEqual(binary_tree_level_traversal_2(self.t2), [[1]])
        self.assertEqual(binary_tree_level_traversal_2(self.t3), [[1], [2, 3]])
        self.assertEqual(binary_tree_level_traversal_2(self.t4), [[1], [3], [2, 4], [5, 6, 7]])