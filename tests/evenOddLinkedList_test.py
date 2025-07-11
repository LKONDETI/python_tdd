from unittest import TestCase
from src.katas.evenOddLinkedList import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TestEvenOddLinkedList(TestCase):
    
    def test_first_five_numbers_nodes(self):
        #head = [1,2,3,4,5]
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(1, ListNode(3, ListNode(5, ListNode(2, ListNode(4)))))
        result = Solution().oddEvenList(head)
        self.assertEqual(self.compare_lists(result, expected), True)
    
    def test_random_numbers_nodes(self):
        #head = [2,1,3,5,6,4,7]
        head = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
        expected = ListNode(2, ListNode(3, ListNode(6, ListNode(7, ListNode(1, ListNode(5, ListNode(4)))))))
        result = Solution().oddEvenList(head)
        self.assertEqual(self.compare_lists(result, expected), True)

    
    def compare_lists(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return l1 is None and l2 is None