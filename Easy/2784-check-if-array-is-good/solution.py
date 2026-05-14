# Problem: #2784 - Check if Array is Good
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/check-if-array-is-good/
# Submitted: 2026-05-14
# Tags: Array, Hash Table, Sorting
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxv = len(nums) - 1
        dic = {}

        for i in nums:
            if i > maxv:
                return False
            dic[i] = dic.get(i, 0) + 1
            if i != maxv and dic[i] == 2:
                return False
        
        return dic[maxv] == 2
            
