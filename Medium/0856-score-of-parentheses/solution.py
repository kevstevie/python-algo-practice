# Problem: #856 - Score of Parentheses
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/score-of-parentheses/
# Submitted: 2026-10-07
# Tags: String, Stack, Bracket Sequences
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]

        for c in s:
            if c == '(':
                st.append(0)
            else:
                inner = st.pop()
                st[-1] += max(inner * 2, 1)
        
        return st[0]
