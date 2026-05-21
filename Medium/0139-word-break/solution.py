# Problem: #139 - Word Break
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/word-break/
# Submitted: 2026-05-21
# Tags: Array, Hash Table, String, Dynamic Programming, Trie, Memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [True] + [False] * n

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
                    
        return dp[n]
