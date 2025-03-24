from typing import List
#prefix sum
#time and space: O(n) and O(1)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        current = 0
        for i in gain:
            current += i
            maxAltitude = max(maxAltitude, current)
        return maxAltitude
    
        """
        Function findHighestAltitude(gain):
    maxAltitude ← 0  // Start at sea level
    currentAltitude ← 0

    For each change in gain:
        currentAltitude ← currentAltitude + change
        maxAltitude ← max(maxAltitude, currentAltitude)

    Return maxAltitude
        """