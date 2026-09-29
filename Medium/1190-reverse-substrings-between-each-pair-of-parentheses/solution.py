# Problem: #1190 - Reverse Substrings Between Each Pair of Parentheses
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# Submitted: 2026-09-29
# Tags: String, Stack, Bracket Sequences
class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = [""]

        for c in s:
            if c == '(':
                st.append("")
                continue
            if c == ')':
                last = st.pop()
                rvs = last[::-1]
                st[-1] += rvs
                continue
            st[-1] += c

        return st[0]
