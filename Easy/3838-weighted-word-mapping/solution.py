# Problem: #3838 - Weighted Word Mapping
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/weighted-word-mapping/
# Submitted: 2026-06-15
# Tags: Array, String, Simulation
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ''

        for i in words:
            temp = 0
            for c in i:
                temp += weights[ord(c) - ord('a')]
            temp %= 26
            temp = 25 - temp
            ans +=  chr(temp + ord('a'))

        return ans 
