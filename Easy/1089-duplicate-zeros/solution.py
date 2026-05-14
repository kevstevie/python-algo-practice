# Problem: #1089 - Duplicate Zeros
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/duplicate-zeros/
# Submitted: 2026-05-14
# Tags: Array, Two Pointers
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        idx = 0
        n = len(arr)
        sub = [0] * n
        for i in arr:
            if idx >= n:
                break
            if i != 0:
                sub[idx] = i
            else:
                sub[idx] = 0
                if idx + 1 < n:
                    sub[idx + 1] = 0
                idx += 1
            idx += 1
        for i in range(n):
            arr[i] = sub[i]
