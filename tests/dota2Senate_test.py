from src.katas.dota2Senate import Solution
from unittest import TestCase


class TestDota2Senate(TestCase):

    def test_case_1(self):
        senate = "RD"
        expected = "Radiant"
        result = Solution().predictPartyVictory(senate)
        self.assertEqual(expected, result)

    def test_case_2(self):
        senate = "RDD"
        expected = "Dire"
        result = Solution().predictPartyVictory(senate)
        self.assertEqual(expected, result)

    def test_case_3(self):
        senate = "RRR"
        expected = "Radiant"
        result = Solution().predictPartyVictory(senate)
        self.assertEqual(expected, result)

    def test_case_4(self):
        senate = "DDD"
        expected = "Dire"
        result = Solution().predictPartyVictory(senate)
        self.assertEqual(expected, result)

    def test_case_5(self):
        senate = "RDRDRD"
        expected = "Radiant"
        result = Solution().predictPartyVictory(senate)
        self.assertEqual(expected, result)