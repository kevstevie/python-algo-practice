# Problem: #912 - Sort an Array
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/sort-an-array/
# Submitted: 2026-04-07
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)
        
        def merge(left, right):
            i = j = 0
            result = []

            while i < len(left) and j < len(right):
                if left[i] >= right[j]:
                    result.append(right[j])
                    j += 1
                else:
                    result.append(left[i])
                    i += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        return merge_sort(nums)
            
