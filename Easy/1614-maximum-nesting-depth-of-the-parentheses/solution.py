# Problem: #1614 - Maximum Nesting Depth of the Parentheses
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# Submitted: 2026-09-29
# Tags: String, Stack, Bracket Sequences
class Solution:
    def maxDepth(self, s: str) -> int:
        cur = 0
        ans = 0

        for c in s:
            if c == '(':
                cur += 1
                ans = max(ans, cur)
            if c == ')':
                cur -= 1

        return ans
