import unittest
import heapq
# ---- Assumptions
#      All the elements in the input array are positive integers.

# ---- Test Cases
#   1) Input: [], 0                                     Output: 0
#   2) Input: [1], 0                                    Output: 0
#   3) Input: [], 1                                     Output: 0
#   4) Input: [5, 1, 1, 3], 1                           Output: 10
#   5) Input: [5, 1, 1, 3], 2                           Output: 5
#   6) Input: [6, 1, 1, 3], 2                           Output: 6
#   7) Input: [2, 2, 5, 6, 1], 2                        Output: 8
#   8) Input: [2, 2, 5, 6, 1], 3                        Output: 6
#   9) Input: [100, 1000, 10, 10000, 1], 5              Output: 10000

# ---- Approach
# Idea:  Use HEAP (PRIORITY-QUEUE) to store the sum of each thread.
# Steps: 1) Sort tasks in reversed order (from largest one to smallest one)
#        2) Initialize an array of t elements representing for the sums of threads and (min)heapify it.
#        3) Iterate sorted tasks, for each task, pop the min number from heap, increase it by the time
#           of this task and push it back to heap.
#        4) Record the max sum during the iteration, which is the total time needed to complete all the tasks
#
# Implementation:
#     t is the number of threads
def fair_distribution_of_tasks(tasks, t):
    if len(tasks) == 0 or t == 0:
        return 0

    tasks.sort(reverse=True)                    # O(n log(n))
    sums = [0] * t
    heapq.heapify(sums)                         # O(n)

    max_time = 0
    for task in tasks:                          # O(n)
        cur_sum = heapq.heappop(sums)           # O(log(n))
        cur_sum += task
        max_time = max(max_time, cur_sum)
        heapq.heappush(sums, cur_sum)           # O(log(n))

    return max_time
# - Complexity
#   Time: O(n log(n)), where n is the length of tasks array, spent on sorting tasks and operations on heap.
#   Space: O(t), where t is the number of threads

class TestMeetingRooms(unittest.TestCase):
    def test_fair_distribution_of_tasks(self):
        self.assertEqual(fair_distribution_of_tasks([], 0), 0)
        self.assertEqual(fair_distribution_of_tasks([1], 0), 0)
        self.assertEqual(fair_distribution_of_tasks([], 1), 0)
        self.assertEqual(fair_distribution_of_tasks([5, 1, 1, 3], 1), 10)
        self.assertEqual(fair_distribution_of_tasks([5, 1, 1, 3], 2), 5)
        self.assertEqual(fair_distribution_of_tasks([6, 1, 1, 3], 2), 6)
        self.assertEqual(fair_distribution_of_tasks([2, 2, 5, 6, 1], 2), 8)
        self.assertEqual(fair_distribution_of_tasks([2, 2, 5, 6, 1], 3), 6)
        self.assertEqual(fair_distribution_of_tasks([100, 1000, 10, 10000, 1], 5), 10000)

if __name__ == '__main__':
    unittest.main()