# Problem: #179 - Largest Number
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/largest-number/
# Submitted: 2026-05-05
# Tags: Array, String, Greedy, Sorting
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(i) for i in nums]
        
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        arr.sort(key=cmp_to_key(compare))
        return "0" if arr[0] == "0" else "".join(arr)
