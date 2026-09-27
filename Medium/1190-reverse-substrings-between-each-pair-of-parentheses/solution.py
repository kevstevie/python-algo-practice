# Problem: #1190 - Reverse Substrings Between Each Pair of Parentheses
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# Submitted: 2026-09-27
# Tags: String, Stack, Bracket Sequences
class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        ans = ""

        for c in s:
            if c == '(':
                st.append("")
                continue
            if c == ')':
                last = st.pop()
                rvs = last[::-1]
                if not st:
                    ans += rvs
                else:
                    st[-1] += rvs
                continue
            if not st:
                ans += c
            else:
                st[-1] += c

        while st:
            ans += st.pop()[::-1]

        return ans
