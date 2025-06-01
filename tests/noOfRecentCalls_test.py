from unittest import TestCase
from src.katas.noOfRecentCalls import RecentCounter

class TestRecentCounter(TestCase):

    def test_example1(self):
        rc = RecentCounter()
        
        output = [
            rc.ping(1),     
            rc.ping(100),    
            rc.ping(3001),   
            rc.ping(3002),   
        ]
        
        expected = [1, 2, 3, 3]
        self.assertEqual(output, expected)
    
    def test_example2(self):
        rc = RecentCounter()
        
        output = [
            rc.ping(100),    
            rc.ping(3001),   
            rc.ping(3002),   
            rc.ping(3003),   
        ]
        
        expected = [1, 2, 3, 4]
        self.assertEqual(output, expected)