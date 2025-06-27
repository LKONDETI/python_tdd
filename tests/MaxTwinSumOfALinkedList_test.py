from unittest import TestCase
from src.katas.MaxTwinSumOfALinkedList import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TestMaxTwinSumOfALinkedList(TestCase):
    
    def test_sum_6(self):
        head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
        expected = 6
        result = Solution().pairSum(head)
        self.assertEqual(result, expected)

    def test_sum_7(self):
        head = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
        expected = 7
        result = Solution().pairSum(head)
        self.assertEqual(result, expected)
    
    def test_two_nodes(self):
        head = ListNode(1, ListNode(100000))
        expected = 100001
        result = Solution().pairSum(head)
        self.assertEqual(result, expected)
    
    def compare_lists(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return l1 is None and l2 is None
    