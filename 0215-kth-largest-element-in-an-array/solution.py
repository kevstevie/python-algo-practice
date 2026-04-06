# Problem: #215 - Kth Largest Element in an Array
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Submitted: 2026-04-06
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in nums:
            heapq.heappush(pq, -i)

        ans = 0

        for _ in range(1, k):
            heapq.heappop(pq)
        
        return -heapq.heappop(pq)
