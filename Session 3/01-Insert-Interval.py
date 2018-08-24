import unittest

# ---- Definition of Interval Class
#      A Interval is a pair of integer time slots representing for the start and end time of an interval
class Interval():
    def __init__(self, start, end):
        self.start = start
        self.end = end

# ---- Test Cases
#   1) Input: [], []                                              Output: []
#   2) Input: [], [1, 4]                                          Output: [[1, 4]]
#   3) Input: [[1, 2]], [3, 4]                                    Output: [[1, 2], [3, 4]]
#   4) Input: [[1, 3]], [2, 4]                                    Output: [[1, 4]]
#   5) Input: [[1, 10], [15, 16], [17, 21], [18, 90]], [9, 17]    Output: [[1, 90]]

# ---- Approach
# Idea: Merge the given interval into the original list first, sort them by start time, and then merge in order
#
# Implementation:
def insert_interval(intervals, new_interval):
    if new_interval is None:
        return intervals

    intervals.append(new_interval)
    intervals.sort(key=lambda x: x.start)

    res = []
    for i in intervals:
        if len(res) == 0 or res[-1].end < i.start:
            res.append(i)
        else:
            res[-1].end = max(res[-1].end, i.end)
    return res
# - Complexity
#   Time: O(n log(n)), spent on sorting input intervals
#   Space: O(n), spent on sorting the intervals


class TestInsertInterval(unittest.TestCase):
    intervals1 = [];               new_interval1 = None
    intervals2 = [];               new_interval2 = Interval(1, 4)
    intervals3 = [Interval(1, 2)]; new_interval3 = Interval(3, 4)
    intervals4 = [Interval(1, 3)]; new_interval4 = Interval(2, 4)
    intervals5 = [Interval(1, 10), Interval(15, 16), Interval(17, 21), Interval(18, 90)]; new_interval5 = Interval(9, 17)
    merged_intervals1 = []
    merged_intervals2 = [Interval(1, 4)]
    merged_intervals3 = [Interval(1, 2), Interval(3, 4)]
    merged_intervals4 = [Interval(1, 4)]
    merged_intervals5 = [Interval(1, 90)]
    def test_insert_interval(self):
        self.assertTrue(self.checkIntervalsEqual(insert_interval(self.intervals1, self.new_interval1),
                                                 self.merged_intervals1))
        self.assertTrue(self.checkIntervalsEqual(insert_interval(self.intervals2, self.new_interval2),
                                                 self.merged_intervals2))
        self.assertTrue(self.checkIntervalsEqual(insert_interval(self.intervals3, self.new_interval3),
                                                 self.merged_intervals3))
        self.assertTrue(self.checkIntervalsEqual(insert_interval(self.intervals4, self.new_interval4),
                                                 self.merged_intervals4))
        self.assertTrue(self.checkIntervalsEqual(insert_interval(self.intervals5, self.new_interval5),
                                                 self.merged_intervals5))

    def checkIntervalsEqual(self, intervals1, intervals2):
        if len(intervals1) != len(intervals2):
            return False
        for i in range(len(intervals1)):
            if intervals1[i].start != intervals2[i].start or intervals1[i].end != intervals2[i].end:
                return False
        return True