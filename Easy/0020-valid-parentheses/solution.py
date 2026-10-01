# Problem: #20 - Valid Parentheses
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/valid-parentheses/
# Submitted: 2026-10-01
# Tags: String, Stack, Bracket Sequences
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in d:
                if st and st[-1] == d[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)

        return not st
