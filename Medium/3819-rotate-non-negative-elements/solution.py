# Problem: #3819 - Rotate Non Negative Elements
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/rotate-non-negative-elements/
# Submitted: 2026-06-22
# Tags: Array, Simulation
class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        pos = []
        for i in nums:
            if i >= 0:
                pos.append(i)
        rot = [0] * len(pos)

        for i in range(len(pos)):
            rot[i] = pos[(i + k) % len(pos)]

        idx = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] = rot[idx]
                idx += 1
        
        return nums
