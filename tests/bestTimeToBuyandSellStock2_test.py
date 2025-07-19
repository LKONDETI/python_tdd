from src.katas.bestTimeToBuyandSellStock2 import Solution
import unittest
#class name and file name should be different
class bestTimeToBuyandSellStock2(unittest.TestCase): 

    
    def test_output_7(self):

        # def should be filename.classname
        result = Solution()
        self.assertEqual(result.maxProfit([7,1,5,3,6,4]), 7)
    
    def test_list_low_to_high(self):
        result = Solution()
        self.assertEqual(result.maxProfit([1,2,3,4,5]), 4)
    
    def test_list_high_to_low(self):
        result = Solution()
        self.assertEqual(result.maxProfit([7,6,4,3,1]), 0)
    