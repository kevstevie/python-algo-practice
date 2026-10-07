# Problem: #921 - Minimum Add to Make Parentheses Valid
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Submitted: 2026-10-07
# Tags: String, Stack, Greedy, Bracket Sequences
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for c in s:
            if c == ')':
                if st and st[-1] == '(':
                    st.pop()
                else:
                    st.append(c)
            else:
                st.append(c)
        
        return len(st)
