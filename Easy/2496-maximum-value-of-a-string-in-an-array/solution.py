# Problem: #2496 - Maximum Value of a String in an Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/
# Submitted: 2026-06-22
# Tags: Array, String
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(i) if i.isdecimal() else len(i) for i in strs)
