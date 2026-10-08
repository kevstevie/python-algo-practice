# Problem: #1021 - Remove Outermost Parentheses
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/remove-outermost-parentheses/
# Submitted: 2026-10-08
# Tags: String, Stack, Bracket Sequences
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cur = 0
        ans = []

        for c in s:
            if c == '(':
                if cur != 0:
                    ans.append(c)
                cur += 1
            if c == ')':
                cur -= 1
                if cur != 0:
                    ans.append(c)

        return ''.join(ans)
