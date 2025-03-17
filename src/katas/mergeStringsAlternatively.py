class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = []
        i, j = 0, 0
        
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged_string.append(word1[i])
                i += 1
            if j < len(word2):
                merged_string.append(word2[j])
                j += 1
        
        return "".join(merged_string)
# Initialize index i = 0, j = 0
# While i < length of word1 OR j < length of word2:
    # If i < length of word1:
        # Append word1[i] to mergedString
        # Increment i
    # If j < length of word2:
        # Append word2[j] to mergedString
        # Increment j
# Return mergedString
