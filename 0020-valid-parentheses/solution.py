# Problem: #20 - Valid Parentheses
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/valid-parentheses/
# Submitted: 2026-04-09
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        os = {"(","{","["}
        cs = {")","}","]"}
        pairs = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in os:
                st.append(i)
            if i in cs:
                if st and st[-1] == pairs[i]:
                    st.pop()
                else:
                    return False

        return not st
