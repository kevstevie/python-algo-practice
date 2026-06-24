# Problem: #1374 - Generate a String With Characters That Have Odd Counts
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
# Submitted: 2026-06-24
# Tags: String
class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return 'a' * (n - 1) +'b'
        else:
            return 'a' * n
