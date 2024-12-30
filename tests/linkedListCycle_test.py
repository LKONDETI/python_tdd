from unittest import TestCase
from src.katas.linkedListCycle import Solution
from src.katas.linkedListCycle import ListNode

class TestHasCycle(TestCase):
    def test_case1(self):
        node1 = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        
        solution = Solution()
        self.assertEqual(solution.hasCycle(node1), True)
    
    def test_case2(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        node2.next = node1
        solution = Solution()
        self.assertEqual(solution.hasCycle(node1), True)
    
    def test_case3(self):
        node1 = ListNode(1)
        solution = Solution()
        self.assertEqual(solution.hasCycle(node1), False)



    