from unittest import TestCase
from src.katas.deleteTheMiddleElementInLinkedList import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TestDeleteTheMiddleElementInTheLinkedList(TestCase):
    
    def test_multiple_node_list(self):
        #head = [1,3,4,7,1,2,6]
        head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
        expected = ListNode(1, ListNode(3, ListNode(4, ListNode(1, ListNode(2, ListNode(6))))))
        result = Solution().deleteMiddle(head)
        self.assertEqual(self.compare_lists(result, expected), True)
        
    def test_single_node_list(self):
        #head = [1]
        head = ListNode(1)
        expected = None
        result = Solution().deleteMiddle(head)
        self.assertEqual(result, expected)
    
    def test_double_node_list(self):
        #head = [1,2]
        head = ListNode(1, ListNode(2))
        expected = ListNode(1)
        result = Solution().deleteMiddle(head)
        self.assertEqual(self.compare_lists(result, expected), True)

    def test_four_nodes_list(self):
        #head = [1,2,3,4]
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        expected = ListNode(1, ListNode(2, ListNode(4)))
        result = Solution().deleteMiddle(head)
        self.assertEqual(self.compare_lists(result, expected), True)

    def compare_lists(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return l1 is None and l2 is None