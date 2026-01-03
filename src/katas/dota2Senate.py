from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque(i for i, p in enumerate(senate) if p == 'R')
        D = deque(i for i, p in enumerate(senate) if p == 'D')

        while R and D:
            radiant, dire = R.popleft(), D.popleft()

            if radiant < dire:
                R.append(radiant + len(senate))
            else:
                D.append(dire + len(senate))
            
        return "Radiant" if R else "Dire"  

# time and space complexity: O(n)
