# Problem: #3184 - Count Pairs That Form a Complete Day I
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/
# Submitted: 2026-09-22
# Tags: Array, Hash Table, Counting
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        n = len(hours)

        for i in range(n):
            for j in range(i + 1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    ans += 1
        return ans
