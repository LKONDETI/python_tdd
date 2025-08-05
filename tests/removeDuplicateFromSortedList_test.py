from unittest import TestCase
from src.katas.removeDuplicateFromSortedList import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TestReverseDuplicateFromSortedList(TestCase):
    
    def test_first_two_nodes(self):
        head = ListNode(1, ListNode(1, ListNode(2)))
        expected = ListNode(1, ListNode(2))
        result = Solution().deleteDuplicates(head)
        self.assertEqual(self.compare_lists(result, expected), True)
    
    def test_no_duplicates(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        expected = ListNode(1, ListNode(2, ListNode(3)))
        result = Solution().deleteDuplicates(head)
        self.assertEqual(self.compare_lists(result, expected), True)
    
    def test_first_three_nodes(self):
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        expected = ListNode(1, ListNode(2, ListNode(3)))
        result = Solution().deleteDuplicates(head)
        self.assertEqual(self.compare_lists(result, expected), True)

    def compare_lists(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return l1 is None and l2 is None