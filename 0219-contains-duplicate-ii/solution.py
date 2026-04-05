# Problem: #219 - Contains Duplicate II
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/contains-duplicate-ii/
# Submitted: 2026-04-05
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i in range(k + 1):
            if i >= len(nums):
                break
            d[nums[i]] = d.get(nums[i], 0) + 1
            if (d[nums[i]] >= 2):
                return True

        for i in range(0, len(nums) - k - 1):
            l = nums[i]
            r = nums[i + k + 1]
            d[l] -= 1
            d[r] = d.get(r, 0) + 1
            if (d[r] >= 2):
                return True

        return False
