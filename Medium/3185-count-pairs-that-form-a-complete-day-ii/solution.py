# Problem: #3185 - Count Pairs That Form a Complete Day II
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/
# Submitted: 2026-09-22
# Tags: Array, Hash Table, Counting
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        m = [0] * 24
        ans = 0

        for i in hours:
            num = i % 24
            need = (24 - num) % 24
            ans += m[need]
            m[num] += 1

        return ans

