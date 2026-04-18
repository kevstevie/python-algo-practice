# Problem: #3783 - Mirror Distance of an Integer
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/mirror-distance-of-an-integer/
# Submitted: 2026-04-18
class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = int(str(n)[::-1])

        return abs(n - rev)
