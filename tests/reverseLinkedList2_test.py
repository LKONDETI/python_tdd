from unittest import TestCase
from src.katas.reverseLinkedList2 import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TestReverseLinkedList2(TestCase):


    def test_multiple_node_list(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        left = 2
        right = 4
        expected = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
        result = Solution().reverseBetween(head, left, right)
        self.assertTrue(self.compare_lists(result, expected))

    

    def test_single_node_list(self):
        head = ListNode(5)
        left = 1
        right = 1
        expected = ListNode(5)
        result = Solution().reverseBetween(head, left, right)
        self.assertTrue(self.compare_lists(result, expected))
    
    def compare_lists(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return l1 is None and l2 is None