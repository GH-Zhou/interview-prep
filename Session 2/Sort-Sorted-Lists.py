import unittest
import heapq

# ---- Definition of ListNode Class
#      A ListNode is a node in the linked list with its value and next property pointing to the next node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Comparator for heapq
    def __lt__(self, other):
        return self.val < other.val

# ---- Test Cases
#   1) Input: None, None                Output: None
#   2) Input: 1 -> 2, None              Output: 1 -> 2
#   3) Input: None, 2 -> 3              Output: 2 -> 3
#   4) Input: 1, 2                      Output: 1 -> 2
#   5) Input: 1 -> 3, 2 -> 4            Output: 1 -> 2 -> 3 -> 4
#   6) Input: 3 -> 4, 1 -> 2            Output: 1 -> 2 -> 3 -> 4
#   7) Input: 1 -> 5, 2 -> 3 -> 4       Output: 1 -> 2 -> 3 -> 4 -> 5
#   8) Input: 2 -> 3 -> 5, 1 -> 4 -> 6  Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6

# ---- Approach
# Idea: Use two pointers to iterate two lists, add the smaller one to the merged list
#
# Implementation:
def sort_two_sorted_lists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1 is None:
        cur.next = l2
    else:
        cur.next = l1
    return dummy.next
# - Complexity
#   Time: O(m + n), spent on iterating two lists
#   Space: O(1), only the references of nodes changed


# ====================================
# ---- FOLLOW UP - Sort K Sorted Lists

# ---- Test Case
#   Input: 1 -> 4 -> 7, 2 -> 5 -> 8, 3 -> 6 -> 9 Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9

# ---- Approach
# Idea: Use a heap to keep track of the currently smallest number among the headers of each list
#
# Implementation:
def sort_k_sorted_lists(lists):
    if lists is None or len(lists) == 0: return None
    h = []
    for l in lists:
        if l:
            heapq.heappush(h, l)

    dummy = ListNode(0)
    cur = dummy
    while len(h) > 0:
        lst = heapq.heappop(h)
        print(lst.val)
        cur.next = lst
        lst = lst.next
        if lst:
            heapq.heappush(h, lst)
        cur = cur.next
    return dummy.next
# - Complexity
#   Time: O(nk(log k)), where n is the average length of k lists
#   Space: O(k), spent on the heap for k headers of the lists


class TestSortSortedLists(unittest.TestCase):
    l11 = None; l12 = None; l1 = None

    l21 = ListNode(1); l21.next = ListNode(2); l22 = None
    l2 = ListNode(1); l2.next = ListNode(2)

    l31 = None; l32 = ListNode(2); l32.next = ListNode(3)
    l3 = ListNode(2); l3.next = ListNode(3)

    l41 = ListNode(1); l42 = ListNode(2)
    l4 = ListNode(1); l4.next = ListNode(2)

    l51 = ListNode(1); l51.next = ListNode(3); l52 = ListNode(2); l52.next = ListNode(4)
    l5 = ListNode(1); l5.next = ListNode(2); l5.next.next = ListNode(3); l5.next.next.next = ListNode(4)

    l61 = ListNode(3); l61.next = ListNode(4); l62 = ListNode(1); l62.next = ListNode(2)
    l6 = ListNode(1); l6.next = ListNode(2); l6.next.next = ListNode(3); l6.next.next.next = ListNode(4)

    l71 = ListNode(1); l71.next = ListNode(5); l72 = ListNode(2); l72.next = ListNode(3); l72.next.next = ListNode(4)
    l7 = ListNode(1); l7.next = ListNode(2); l7.next.next = ListNode(3); l7.next.next.next = ListNode(4)
    l7.next.next.next.next = ListNode(5)

    l81 = ListNode(2); l81.next = ListNode(3); l81.next.next = ListNode(5)
    l82 = ListNode(1); l82.next = ListNode(4); l82.next.next = ListNode(6)
    l8 = ListNode(1); l8.next = ListNode(2); l8.next.next = ListNode(3); l8.next.next.next = ListNode(4)
    l8.next.next.next.next = ListNode(5); l8.next.next.next.next.next = ListNode(6)

    def test_sort_two_sorted_lists(self):
        self.assertTrue(self.check_list_equal(sort_two_sorted_lists(self.l11, self.l12), self.l1))
        self.assertTrue(self.check_list_equal(sort_two_sorted_lists(self.l21, self.l22), self.l2))
        self.assertTrue(self.check_list_equal(sort_two_sorted_lists(self.l31, self.l32), self.l3))
        self.assertTrue(self.check_list_equal(sort_two_sorted_lists(self.l41, self.l42), self.l4))
        self.assertTrue(self.check_list_equal(sort_two_sorted_lists(self.l51, self.l52), self.l5))
        self.assertTrue(self.check_list_equal(sort_two_sorted_lists(self.l61, self.l62), self.l6))
        self.assertTrue(self.check_list_equal(sort_two_sorted_lists(self.l71, self.l72), self.l7))
        self.assertTrue(self.check_list_equal(sort_two_sorted_lists(self.l81, self.l82), self.l8))

    list1 = ListNode(1); list1.next = ListNode(4); list1.next.next = ListNode(7)
    list2 = ListNode(2); list2.next = ListNode(5); list2.next.next = ListNode(8)
    list3 = ListNode(3); list3.next = ListNode(6); list3.next.next = ListNode(9)

    list = ListNode(1);  list.next = ListNode(2);  list.next.next = ListNode(3)
    list.next.next.next = ListNode(4);   list.next.next.next.next = ListNode(5)
    list.next.next.next.next.next = ListNode(6)
    list.next.next.next.next.next.next = ListNode(7)
    list.next.next.next.next.next.next.next = ListNode(8)
    list.next.next.next.next.next.next.next.next = ListNode(9)

    def test_sort_k_sorted_lists(self):
        self.assertTrue(self.check_list_equal(sort_k_sorted_lists([self.list1, self.list2, self.list3]), self.list))

    def check_list_equal(self, l1, l2):
        p1, p2 = l1, l2
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next; p2 = p2.next
        return p1 is None and p2 is None

if __name__ == '__main__':
    unittest.main()