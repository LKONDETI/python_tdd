from unittest import TestCase
from src.katas.reverseLinkedList import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TestReverseLinkedList(TestCase):
    
    def test_multiple_node_list(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
        result = Solution().reverseList(head)
        self.assertEqual(self.compare_lists(result, expected), True)
    

    def test_double_node_list(self):
        head = ListNode(1, ListNode(2))
        expected = ListNode(2, ListNode(1))
        result = Solution().reverseList(head)
        self.assertTrue(self.compare_lists(result, expected))
    
    def compare_lists(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return l1 is None and l2 is None
    
    
