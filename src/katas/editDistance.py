class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Create the DP table
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # Deletion
                        dp[i][j - 1],     # Insertion
                        dp[i - 1][j - 1]  # Replacement
                    )

        return dp[m][n]
#time complexity: O(m * n)
#space complexity: O(m * n)
# approach: Dynamic Programming