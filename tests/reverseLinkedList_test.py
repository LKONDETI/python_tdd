from unittest import TestCase
from src.katas.reverseLinkedList import Solution

class TestReverseLinkedList(TestCase):

    def test_single_item(self):
        LinkedNode = [1, 2, 3, 4, 5]
        result = Solution()
        self.assertEqual(result.reverseList(LinkedNode, [5, 4, 3, 2, 1]))