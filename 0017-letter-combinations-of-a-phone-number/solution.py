# Problem: #17 - Letter Combinations of a Phone Number
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Submitted: 2026-04-09
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }
        res = []
        def backtrack(arr, a, b):
            if len(arr) == len(digits):
                res.append("".join(arr))
                return

            num = phone[digits[a]]
            for j in range(b, len(num)):
                arr.append(num[j])
                backtrack(arr, a + 1, b)
                arr.pop()


        backtrack([], 0, 0)
        return res
