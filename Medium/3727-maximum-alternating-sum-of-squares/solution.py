# Problem: #3727 - Maximum Alternating Sum of Squares
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/maximum-alternating-sum-of-squares/
# Submitted: 2026-10-14
# Tags: Array, Greedy, Sorting
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        l = []
        n = len(nums)
        for i in nums:
            l.append(abs(i))
        l.sort()
        dq = deque(l)    
        ans = 0
        for i in range(n):
            if i % 2 == 0:
                ans += dq.pop() ** 2
            else:
                ans -= dq.popleft() ** 2
        return ans
