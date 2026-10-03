# Problem: #32 - Longest Valid Parentheses
# Difficulty: Hard
# Language: Python3
# URL: https://leetcode.com/problems/longest-valid-parentheses/
# Submitted: 2026-10-03
# Tags: String, Dynamic Programming, Stack, Bracket Sequences
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        st = []
        dp = [0] * n
        ans = 0

        for i in range(n):
            c = s[i]
            if c == ')' and st and st[-1][0] == '(':
                prev = st.pop()
                dp[prev[1]] = 1
                dp[i] = 1
            else:
                st.append((c, i))

        for i in range(n):
            if dp[i] == 1 and i >= 1:
                dp[i] = dp[i - 1] + 1
            ans = max(ans, dp[i])

        return ans
