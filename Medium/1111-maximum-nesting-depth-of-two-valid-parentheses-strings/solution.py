# Problem: #1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
# Submitted: 2026-09-30
# Tags: String, Stack, Bracket Sequences
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        cur = 0

        for c in seq:
            if c == '(':
                cur += 1
                ans.append(cur % 2)
            else:
                ans.append(cur % 2)
                cur -= 1

        return ans
