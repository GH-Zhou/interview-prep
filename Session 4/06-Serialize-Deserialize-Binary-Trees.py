import unittest, collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ---- Assumptions
#      Use a pound sign (#) to indicate a null node

# -----------------------------------------------------------------------------------
# ---- Approach 1 (with test case)
# Idea: During serialization, initialize an array (with resizing if exceeding the maximum capacity),
#       and then join it into a string using the delimiter ",";
#       During deserialization, split the input string into an array and use the array to regenerate
#       the tree;
#       Think of heap, the root is located at index 0, and for each node i, its left child will be at
#       index 2i + 1, and its right child at index 2i + 2.

#      (Serialize)
#   1) Input: None        --------->   Output: ""
#   2) Input:  1          --------->   Output: "1"
#   3) Input:  1          --------->   Output: "1,2,3"
#             / \
#            2   3
#   4) Input:  1          --------->   Output: "1,#,3,#,#,2,4,#,#,#,#,5,#,6,7"
#               \
#                3
#               / \
#              2   4
#             /   / \
#            5   6   7

INIT_CAPACITY = 4
SCALE_FACTOR = 2

def serialize_1(root):
    if root is None:
        return ""
    array = ["#"] * INIT_CAPACITY
    q = collections.deque([(root, 0)])
    max_index = 0
    while q:
        node, index = q.popleft()

        if index >= len(array):  # if the index is exceeding the capacity of array
            # resize array by appending None elements in doubled size of its original length.
            array += ["#"] * (SCALE_FACTOR * len(array))

        if node:
            array[index] = str(node.val)
            max_index = max(max_index, index)
            q.append((node.left, 2 * index + 1))
            q.append((node.right, 2 * index + 2))
    return ",".join(array[:(max_index+1)])

#      (Deserialize)
#   1) Output: None       <---------    Input: ""
#   2) Output:  1         <---------    Input: "1"
#   3) Output:  1         <---------    Input: "1,2,3"
#              / \
#             2   3
#   4) Output:  1         <---------    Input: "1,#,3,#,#,2,4,#,#,#,#,5,#,6,7"
#                \
#                 3
#                / \
#               2   4
#              /   / \
#             5   6   7

def deserialize_1(string):
    def dfs(root, index):
        if root:
            if 2 * index + 1 < len(array):
                root.left = None if array[2 * index + 1] == "#" else TreeNode(int(array[2 * index + 1]))
            if 2 * index + 2 < len(array):
                root.right = None if array[2 * index + 2] == "#" else TreeNode(int(array[2 * index + 2]))
            dfs(root.left, 2 * index + 1)
            dfs(root.right, 2 * index + 2)

    if string == "":
        return None
    array = string.split(",")
    root = TreeNode(int(array[0]))
    dfs(root, 0)
    return root

# ---- Complexity
#      Time: O(2 ^ h), where h is the height of the binary tree
#                      (O(number of nodes in perfect binary tree with a height h))
#      Space: O(2 ^ h)

# -----------------------------------------------------------------------------------
# ---- Approach 2 (with test case)
# Idea: Similar to Approach 1 but use less space by removing unnecessary null nodes
#

#      (Serialize)
#   1) Input: None        --------->   Output: ""
#   2) Input:  1          --------->   Output: "1"
#   3) Input:  1          --------->   Output: "1,2,3"
#             / \
#            2   3
#   4) Input:  1          --------->   Output: "1,#,3,2,4,5,#,6,7"
#               \
#                3
#               / \
#              2   4
#             /   / \
#            5   6   7

def serialize_2(root):
    if root is None:
        return ""
    array = []
    q = collections.deque([root])

    while q:
        level_length = len(q)  # traverse tree level by level
        leaves_count = 0  # used for avoiding recording trailing null nodes

        for i in range(level_length):
            node = q.popleft()
            if node:
                array.append(str(node.val))
                if not node.left and not node.right:
                    leaves_count += 1
                q.append(node.left)
                q.append(node.right)
            else:
                array.append("#")

        # When leaves_count * 2 equals to the length of q,
        # it means there're only null nodes in q currently, thus stop here.
        if leaves_count * 2 == len(q):
            break

    return ",".join(array)

#      (Deserialize)
#   1) Output: None       <---------    Input: ""
#   2) Output:  1         <---------    Input: "1"
#   3) Output:  1         <---------    Input: "1,2,3"
#              / \
#             2   3
#   4) Output:  1         <---------    Input: "1,#,3,2,4,5,#,6,7"
#                \
#                 3
#                / \
#               2   4
#              /   / \
#             5   6   7

def deserialize_2(string):
    if string == "":
        return None
    array = string.split(",")
    root = TreeNode(int(array[0]))
    q = collections.deque([root])

    i = 1
    while q:
        level_length = len(q)  # traverse tree level by level
        for _ in range(level_length):
            node = q.popleft()
            if node:
                if i < len(array):
                    node.left = None if array[i] == "#" else TreeNode(int(array[i]))
                i += 1

                if i < len(array):
                    node.right = None if array[i] == "#" else TreeNode(int(array[i]))
                i += 1

                q.append(node.left)
                q.append(node.right)
    return root

# ---- Complexity
#      Time: O(n), where n is the number of nodes
#      Space: O(n), where n is the number of nodes


class TestSerializeDeserialize(unittest.TestCase):
    t1 = None

    t2 = TreeNode(1)

    t3 = TreeNode(1); t3.left = TreeNode(2); t3.right = TreeNode(3)

    t4 = TreeNode(1); t4.right = TreeNode(3); t4.right.left = TreeNode(2); t4.right.left.left = TreeNode(5)
    t4.right.right = TreeNode(4); t4.right.right.left = TreeNode(6); t4.right.right.right = TreeNode(7)

    def test_serialize_deserialize_1(self):
        self.assertTrue(self.trees_equal(deserialize_1(serialize_1(self.t1)), self.t1))
        self.assertTrue(self.trees_equal(deserialize_1(serialize_1(self.t2)), self.t2))
        self.assertTrue(self.trees_equal(deserialize_1(serialize_1(self.t3)), self.t3))
        self.assertTrue(self.trees_equal(deserialize_1(serialize_1(self.t4)), self.t4))

    def test_serialize_deserialize_2(self):
        self.assertTrue(self.trees_equal(deserialize_2(serialize_2(self.t1)), self.t1))
        self.assertTrue(self.trees_equal(deserialize_2(serialize_2(self.t2)), self.t2))
        self.assertTrue(self.trees_equal(deserialize_2(serialize_2(self.t3)), self.t3))
        self.assertTrue(self.trees_equal(deserialize_2(serialize_2(self.t4)), self.t4))

    def trees_equal(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2:
            return root1.val == root2.val and self.trees_equal(root1.left, root2.left) \
                   and self.trees_equal(root1.right, root2.right)
        return False
