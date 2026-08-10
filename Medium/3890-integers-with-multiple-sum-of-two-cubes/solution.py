# Problem: #3890 - Integers With Multiple Sum of Two Cubes
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/
# Submitted: 2026-08-10
# Tags: Hash Table, Sorting, Counting, Enumeration
class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        maxv = math.ceil(n ** (1/3))
        d = {}
        for i in range(1, maxv + 1):
            for j in range(i, maxv + 1):
                res = i ** 3 + j ** 3
                d[res] = d.get(res, 0) + 1
        
        return sorted([k for k, v in d.items() if v >= 2 and k <= n])
