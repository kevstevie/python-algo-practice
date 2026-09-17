# Problem: #1385 - Find the Distance Value Between Two Arrays
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Submitted: 2026-09-17
# Tags: Array, Two Pointers, Binary Search, Sorting
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i in arr1:
            temp = 0
            for j in arr2:
                if abs(i - j) > d:
                    temp += 1
            if temp == len(arr2):
                ans += 1
            temp = 0
        return ans
                
