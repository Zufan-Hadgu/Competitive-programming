# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            if word1[i - 1] == word2[j - 1]:
                return dp(i - 1, j - 1)
            return 1 + min(
                dp(i, j - 1),
                dp(i - 1, j),
                dp(i - 1, j - 1)
            )
        
        return dp(len(word1), len(word2))

        