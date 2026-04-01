from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        cursor = 0
        val = nums[0]

        while idx < len(nums):
            while cursor < len(nums) and nums[cursor] == val:
                cursor += 1

            nums[idx] = val
            idx += 1
            if cursor == len(nums):
                break

            val = nums[cursor]

        return idx
