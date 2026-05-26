# Problem: #3120 - Count the Number of Special Characters I
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/count-the-number-of-special-characters-i/
# Submitted: 2026-05-26
# Tags: Hash Table, String
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = set()
        s = set()

        for i in word:
            c = ord(i)
            if c >= ord('a') and c <= ord('z'):
                if chr(c - ord('a') + ord('A')) in s:
                    ans.add(i)
            else:
                if chr(c - ord('A') + ord('a')) in s:
                    ans.add(chr(c - ord('A') + ord('a')))
            s.add(i)

        return len(ans)
