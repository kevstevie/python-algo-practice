# Problem: #3513 - Number of Unique XOR Triplets I
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/number-of-unique-xor-triplets-i/
# Submitted: 2026-07-23
# Tags: Array, Math, Bit Manipulation
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        return n if n < 3 else 1 << n.bit_length()
        
