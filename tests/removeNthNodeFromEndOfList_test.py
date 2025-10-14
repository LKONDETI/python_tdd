from unittest import TestCase
from src.katas.removeNthNodeFromEndOfList import Solution
from src.katas.removeNthNodeFromEndOfList import ListNode

class TestAddTwoNumbers(TestCase):
    def test_case1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        n = 2
        solution = Solution()
        result = solution.removeNthFromEnd(head, n)
        
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
        
        self.assertEqual(self.linked_list_to_list(result), self.linked_list_to_list(expected))
    
    def test_case2(self):
        head = ListNode(1)
        n = 1
        solution = Solution()
        result = solution.removeNthFromEnd(head, n)
        
        expected = None
        
        self.assertEqual(self.linked_list_to_list(result), self.linked_list_to_list(expected))
    
    def test_case3(self):
        head = ListNode(1, ListNode(2))
        n = 1
        solution = Solution()
        result = solution.removeNthFromEnd(head, n)
        
        expected = ListNode(1)
        
        self.assertEqual(self.linked_list_to_list(result), self.linked_list_to_list(expected))
    
    
    def linked_list_to_list(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    