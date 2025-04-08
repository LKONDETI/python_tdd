from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # solution 1 space:O(1)
        empty = 0 if flowerbed[0] else 1
        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)
                empty =0
            else:
                empty += 1
        n -= (empty) // 2
        return n <= 0      



        """
        solution 2 O(n)
        f = [0] + flowerbed + [0]
        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0 """