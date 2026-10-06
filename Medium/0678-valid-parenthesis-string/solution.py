# Problem: #678 - Valid Parenthesis String
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/valid-parenthesis-string/
# Submitted: 2026-10-06
# Tags: String, Dynamic Programming, Stack, Greedy, Bracket Sequences
class Solution:
    def checkValidString(self, s: str) -> bool:
        rev = s[::-1]
        cnt = 0
        f1 = False
        f2 = False
        for c in s:
            if c in '(*':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                return False
        cnt = 0
        for c in rev:
            if c in ')*':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                return False


        return True
