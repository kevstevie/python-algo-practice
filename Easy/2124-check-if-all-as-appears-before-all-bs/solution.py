# Problem: #2124 - Check if All A's Appears Before All B's
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
# Submitted: 2026-11-24
# Tags: String
class Solution:
    def checkString(self, s: str) -> bool:
        eb = False

        for c in s:
            if eb and c == 'a':
                return False
            if c == 'b':
                eb = True

        return True
