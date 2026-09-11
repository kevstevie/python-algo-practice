# Problem: #3483 - Unique 3-Digit Even Numbers
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/unique-3-digit-even-numbers/
# Submitted: 2026-09-11
# Tags: Array, Hash Table, Recursion, Enumeration
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        l = set()
        n = len(digits)

        for i in range(n):
            hun = digits[i] * 100
            for j in range(n):
                if i == j:
                    continue
                ten = digits[j] * 10
                for k in range(n):
                    if k == j or k == i:
                        continue
                    one = digits[k]

                    l.add(hun + ten + one)

        return sum(1 for x in l if x >= 100 and x % 2 == 0)

        

        

        
