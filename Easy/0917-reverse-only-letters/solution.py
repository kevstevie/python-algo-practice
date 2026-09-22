# Problem: #917 - Reverse Only Letters
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/reverse-only-letters/
# Submitted: 2026-09-22
# Tags: Two Pointers, String
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        st_c = []
        is_c = []

        def is_letter(c):
            return ord('Z') >= ord(c) >= ord('A') or ord('z') >= ord(c) >= ord('a')
        for c in s:
            if is_letter(c):
                is_c.append(True)
                st_c.append(c)
        
        return ''.join([st_c.pop() if is_letter(s[i]) else s[i] for i in range(len(s))])
