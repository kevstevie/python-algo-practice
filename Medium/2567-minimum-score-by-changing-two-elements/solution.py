# Problem: #2567 - Minimum Score by Changing Two Elements
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/minimum-score-by-changing-two-elements/
# Submitted: 2026-11-19
# Tags: Array, Greedy, Sorting
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()

        return min(nums[-1] - nums[2], nums[-3] - nums[0], nums[-2] - nums[1])
