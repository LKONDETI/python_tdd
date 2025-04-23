class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_counts = {}
        magazine_counts = {}
        for char in ransomNote:
            if char in note_counts:
                note_counts[char] += 1
            else:
                note_counts[char] = 1
        for character in magazine:
            if character in magazine_counts:
                magazine_counts[character] += 1
            else:
                magazine_counts[character] = 1
        for char in note_counts:
            if char not in magazine_counts or note_counts[char] > magazine_counts[char]:
                return False
    
        return True
