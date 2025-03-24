from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countInt = {} 
        for num in arr:
            countInt[num] = countInt.get(num, 0) + 1

        occurrences = set() 

        for freq in countInt.values():  # Step 4: Check for duplicates
            if freq in occurrences:
                return False  # Duplicate frequency found
            occurrences.add(freq)

        return True 
"""
1. Create an empty hash map (dictionary) 'countInt' to store integer counts.
2. Iterate through the given array:
   - If the integer is not in 'countInt', add it with value 1.
   - Otherwise, increment its count.
3. Create an empty hash set 'occurrences' to store unique frequencies.
4. Iterate through the values in 'countInt':
   - If the value (frequency) is already in 'occurrences', return False.
   - Otherwise, add the value to 'occurrences'.
5. If all frequencies are unique, return True.

"""
#time and space complexity is O(n) and O(n) respectively

        