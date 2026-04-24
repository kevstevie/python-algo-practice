# Problem: #150 - Evaluate Reverse Polish Notation
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Submitted: 2026-04-24
# Tags: Array, Math, Stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for i in tokens:
            if i in ["+", "*", "/", "-"]:
                s = st.pop()
                f = st.pop()
                if i == "+":
                    st.append(f + s)
                if i == "*":
                    st.append(f * s)
                if i == "/":
                    st.append(int(f / s))
                if i == "-":
                    st.append(f - s)
            else:
                st.append(int(i))

        return st[0]
