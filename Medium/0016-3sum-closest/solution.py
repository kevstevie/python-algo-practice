# Problem: #16 - 3Sum Closest
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/3sum-closest/
# Submitted: 2026-07-26
# Tags: Array, Two Pointers, Sorting
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n = len(nums)
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                sub = abs(res - target)
                if sub <= abs(ans - target):
                    ans = res
                if res < target:
                    l += 1
                else:
                    r -= 1
        return ans
                    
