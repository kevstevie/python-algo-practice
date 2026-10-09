# Problem: #1541 - Minimum Insertions to Balance a Parentheses String
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
# Submitted: 2026-10-09
# Tags: String, Stack, Greedy, Bracket Sequences
class Solution:
    def minInsertions(self, s: str) -> int:
        conv = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                conv.append(c)
            if c == ')':
                if conv and conv[-1] == ')':
                    conv.pop()
                    conv.append('*')
                else:
                    conv.append(c)

        st = []
        ans = 0

        for c in conv:
            if c == '*':
                if st and st[-1] == '(':
                    st.pop()
                else:
                    ans += 1
            if c == ')':
                if st and st[-1] == '(':
                    st.pop()
                    ans += 1
                else:
                    ans += 2
            if c == '(':
                st.append(c)

        ans += len(st) * 2

        return ans
