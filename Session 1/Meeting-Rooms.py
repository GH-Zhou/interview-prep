import unittest
# ---- Assumptions
#      1) (1, 2) and (2, 3) are not considered as overlapping
#      2) One meeting will end first and then another meeting will be started if start time of one meeting
#         and end time of another meeting shares the same slot like (1, 2) and (2, 3).

# ---- Definition of SlotPair Class
#      A SlotPair is a pair of integer time slots representing for the start and end time of a meeting
class SlotPair():
    def __init__(self, start, end):
        self.start = start
        self.end = end

# ---- Test Cases
#   A SlotPair in test cases are represented by a tuple "()"
#   1) Input: []                                        Output: 0
#   2) Input: [(0, 1)]                                  Output: 1
#   3) Input: [(0, 1), (1, 2)]                          Output: 1
#   4) Input: [(0, 1), (0, 1)]                          Output: 2
#   5) Input: [(0, 2), (1, 2)]                          Output: 2
#   6) Input: [(0, 5), (1, 2), (1, 3), (2, 4), (4, 6)]  Output: 3

# ---- Approach 1
# Idea: put all the slots in one array with start/end labeled, sort by the slot regardless of start/end
#       and loop the array to count the number of rooms needed
# Implementation:
def meeting_rooms_1(slotPairs):
    if len(slotPairs) == 0: return 0

    numberOfRooms = 0
    maxRooms = 0
    slots = []
    for pair in slotPairs:
        slots.append((pair.start, True)) # True as Start
        slots.append((pair.end, False))  # False as End

    slots.sort(key=lambda x: (x[0], x[1])) # Sort by the first item (slot) of tuple,
                                           # then by labels for start/end - end (False) first, then start (True)

    for slot, isStart in slots:
        if isStart:
            numberOfRooms += 1
            maxRooms = max(maxRooms, numberOfRooms)
        else:
            numberOfRooms -= 1
    return maxRooms
# - Complexity
#   Time: O(2n log2n) = O(n logn), where n is the length of the input array
#   Space: O(n), where n is the length of the input array


# ---- Approach 2
# Idea: put the start and end slots in two separate arrays, and sort them respectively. Loop through start slots,
#       check the number of available rooms first and then add a new room if there's no room available, and use
#       the existing one if there's at least one available.
# Implementation:
def meeting_rooms_2(slotPairs):
    if len(slotPairs) == 0: return 0

    maxRooms = 0
    available = 0
    end = 0
    starts = []
    ends = []
    for pair in slotPairs:
        starts.append(pair.start)
        ends.append(pair.end)

    starts.sort()
    ends.sort()

    for start in starts:
        while ends[end] <= start:
            end += 1
            available += 1
        if available == 0:
            maxRooms += 1
        else:
            available -= 1
    return maxRooms
# - Complexity
#   Time: O(2n logn) = O(n logn), where n is the length of the input array
#   Space: O(n), where n is the length of the input array

# ---- Trade off
#   Both of the two algorithms run in O(n logn) time, however, the first approach would actually run slower
#   because we need to sort 2n elements for once compared with sort n elements for twice in the second approach.
#   The first approach is easier to come up with and to implement because we only need to consider either
#   increasing one room or decreasing one based on whether it's a start or end slot. The second one introduces
#   a variable "available" which will control whether maxRooms should increase. Since they share the same time /
#   space complexities, the first approach, a more intuitive approach is preferred.

class TestMeetingRooms(unittest.TestCase):
    slot1 = SlotPair(0, 1)
    slot2 = SlotPair(1, 2)
    slot3 = SlotPair(0, 2)
    slot4 = SlotPair(0, 5)
    slot5 = SlotPair(1, 3)
    slot6 = SlotPair(2, 4)
    slot7 = SlotPair(4, 6)
    slotPairs1 = []
    slotPairs2 = [slot1]
    slotPairs3 = [slot1, slot2]
    slotPairs4 = [slot1, slot1]
    slotPairs5 = [slot2, slot3]
    slotPairs6 = [slot2, slot4, slot5, slot6, slot7]

    def test_meeting_rooms_1(self):
        self.assertEqual(meeting_rooms_1(self.slotPairs1), 0)
        self.assertEqual(meeting_rooms_1(self.slotPairs2), 1)
        self.assertEqual(meeting_rooms_1(self.slotPairs3), 1)
        self.assertEqual(meeting_rooms_1(self.slotPairs4), 2)
        self.assertEqual(meeting_rooms_1(self.slotPairs5), 2)
        self.assertEqual(meeting_rooms_1(self.slotPairs6), 3)

    def test_meeting_rooms_2(self):
        self.assertEqual(meeting_rooms_2(self.slotPairs1), 0)
        self.assertEqual(meeting_rooms_2(self.slotPairs2), 1)
        self.assertEqual(meeting_rooms_2(self.slotPairs3), 1)
        self.assertEqual(meeting_rooms_2(self.slotPairs4), 2)
        self.assertEqual(meeting_rooms_2(self.slotPairs5), 2)
        self.assertEqual(meeting_rooms_2(self.slotPairs6), 3)

if __name__ == '__main__':
    unittest.main()