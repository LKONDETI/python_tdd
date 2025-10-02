from unittest import TestCase
from src.katas.addTwoNumbers import Solution
from src.katas.addTwoNumbers import ListNode

class TestAddTwoNumbers(TestCase):
    def test_case1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        solution = Solution()
        result = solution.addTwoNumbers(l1, l2)
        
        expected = ListNode(7, ListNode(0, ListNode(8)))
        
        self.assertTrue(self.compare_linked_lists(result, expected))
    
    def test_case2(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        solution = Solution()
        result = solution.addTwoNumbers(l1, l2)
        
        expected = ListNode(0)
        
        self.assertTrue(self.compare_linked_lists(result, expected))
        
    def compare_linked_lists(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return l1 is None and l2 is None
    