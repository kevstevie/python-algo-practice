# Problem: #3737 - Count Subarrays With Majority Element I
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/count-subarrays-with-majority-element-i/
# Submitted: 2026-06-25
# Tags: Array, Hash Table, Divide and Conquer, Segment Tree, Merge Sort, Counting, Prefix Sum
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                nums[i] = 1
            else:
                nums[i] = 0
        for i in range(1, n):
            nums[i] += nums[i - 1]
        ans = 0
        nums = [0] + nums

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if (j - i + 1) // 2 < nums[j] - nums[i - 1]:
                    ans += 1

        return ans
