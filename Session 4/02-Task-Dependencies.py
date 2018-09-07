import collections, unittest

Dependency = collections.namedtuple('Dependency', ('dep_from', 'dep_on'))

# ---- Assumptions
#      1. If Task A is dependent on B, the input will be a tuple with dep_from being A and dep_on being B
#      2. The number of tasks will not exceed 26.

# ---- Input Format
# ---- Param 1. An array of dependencies.
# ---- Param 2. Total number of tasks (n), assigned from 'A' to chr(ord('A') + n - 1)

# ---- Test Cases
#   1) Input: [], 0                  Output: []
#   2) Input: [], 1                  Output: ['A']
#   3) Input: [('A', 'B')], 2        Output: ['B', 'A']
#   4) Input: [('A', 'B')], 3        Output: ['B', 'C', 'A']
#   5) Input: [('A', 'B'), ('B', 'C')], 4        Output: ['C', 'D', 'B', 'A']
#   6) Input: [('A', 'B'), ('C', 'B')], 4        Output: ['B', 'D', 'A', 'C']

# ---- Approach
# Idea: Use topological sort to reorder the tasks based on dependencies.
#       Treat each task as a node and dependency as an edge.
#
# Implementation:

def task_dependencies(dependencies, task_num):

    if task_num == 0: return []

    graph = [[] for _ in range(task_num)]
    indegrees = [0] * task_num

    # Generate the graph for dependencies and count indegrees for each node
    for dependency in dependencies:
        graph[ord(dependency.dep_on) - ord('A')].append(ord(dependency.dep_from) - ord('A'))
        indegrees[ord(dependency.dep_from) - ord('A')] += 1

    # Initialize a queue recording the task index of zero indegree
    q = collections.deque([])
    for i, indegree in enumerate(indegrees):
        if indegree == 0:
            q.append(i)

    # Use BFS to traverse the graph and only convert task indices to letters when forming the result
    res = []
    while q:
        task = q.popleft()
        res.append(chr(task + ord('A')))
        for next_task in graph[task]:
            indegrees[next_task] -= 1
            if indegrees[next_task] == 0:
                q.append(next_task)
    return res
# ---- Complexity
#   Time:  O(|V| + |E|), where |V| is the number of tasks, and |E| is the length of the given dependencies
#   Space: O(|V| + |E|), spent on the graph and indegrees arrays


class TestTaskDependencies(unittest.TestCase):

    dependencies1 = [Dependency('A', 'B')]
    dependencies2 = [Dependency('A', 'B'), Dependency('B', 'C')]
    dependencies3 = [Dependency('A', 'B'), Dependency('C', 'B')]

    def test_task_dependencies(self):
        self.assertEqual(task_dependencies([], 0), [])
        self.assertEqual(task_dependencies([], 1), ['A'])
        self.assertEqual(task_dependencies(self.dependencies1, 2), ['B', 'A'])
        self.assertEqual(task_dependencies(self.dependencies1, 3), ['B', 'C', 'A'])
        self.assertEqual(task_dependencies(self.dependencies2, 4), ['C', 'D', 'B', 'A'])
        self.assertEqual(task_dependencies(self.dependencies3, 4), ['B', 'D', 'A', 'C'])