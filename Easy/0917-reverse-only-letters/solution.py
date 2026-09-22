# Problem: #917 - Reverse Only Letters
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/reverse-only-letters/
# Submitted: 2026-09-22
# Tags: Two Pointers, String
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        st_c = []

        def is_letter(c):
            return 'Z' >= c >= 'A' or 'z' >= c >= 'a'
            
        for c in s:
            if is_letter(c):
                st_c.append(c)
        
        return ''.join(st_c.pop() if is_letter(s[i]) else s[i] for i in range(len(s)))
