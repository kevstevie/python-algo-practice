# Problem: #977 - Squares of a Sorted Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/squares-of-a-sorted-array/
# Submitted: 2026-04-08
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x ** 2 for x in nums])
        
