# Problem: #1679 - Max Number of K-Sum Pairs
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/max-number-of-k-sum-pairs/
# Submitted: 2026-06-22
# Tags: Array, Hash Table, Two Pointers, Sorting
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = {}

        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        ans = 0

        for i in dic.keys():
            if k % 2 == 0 and k // 2 == i and k // 2 in dic:
                ans += dic[i] // 2
                continue
            if k - i in dic:
                v = min(dic[i], dic[k - i])
                ans += v
                dic[i] -= v
                dic[k - i] -= v

        return ans
