from typing import List
from collections import defaultdict
class Solution:
    #time and space complexity is O(n^2
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        pairs = 0
        n = len(grid)
        for row in grid:
            rows[tuple(row)] += 1
        for col in range(n):
            column = tuple(grid[r][col] for r in range(n))
            if column in rows:
                pairs += rows[column]
        return pairs
        