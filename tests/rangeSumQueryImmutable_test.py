from src.katas.rangeSumQueryImmutable import NumArray
from unittest import TestCase


class TestRangeSumQueryImmutable(TestCase):
    
    def test_simple_range_query(self):
        num_array = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(num_array.sumRange(0, 2), 1)
        self.assertEqual(num_array.sumRange(2, 5), -1)
        self.assertEqual(num_array.sumRange(0, 5), -3)
    