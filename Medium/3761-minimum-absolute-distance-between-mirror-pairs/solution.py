# Problem: #3761 - Minimum Absolute Distance Between Mirror Pairs
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/
# Submitted: 2026-04-17
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        ans = float('inf')

        def reverse(a):
            return int(str(a)[::-1])
        for i in range(n):
            num = nums[i]
            rev = reverse(num)
            if num in memo:
                ans = min(ans, i - memo[num])

            memo[rev] = i
                
        return ans if ans != float('inf') else -1
