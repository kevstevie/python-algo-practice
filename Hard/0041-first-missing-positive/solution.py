# Problem: #41 - First Missing Positive
# Difficulty: Hard
# Language: Python3
# URL: https://leetcode.com/problems/first-missing-positive/
# Submitted: 2026-05-12
# Tags: Array, Hash Table
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            v = nums[i]
            to = nums[i] - 1
            while 1 <= v and v <= n:
                if nums[i] == nums[to]:
                    break
                nums[i], nums[to] = nums[to], nums[i]
                v = nums[i]
                to = v - 1

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1
