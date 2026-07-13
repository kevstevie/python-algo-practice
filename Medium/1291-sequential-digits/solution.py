# Problem: #1291 - Sequential Digits
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/sequential-digits/
# Submitted: 2026-07-13
# Tags: Enumeration
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        cur = 1
        d = 1
        digit = len(str(low))
        plus = 1

        while d < digit:
            d += 1
            l = cur % 10
            cur = cur * 10 + l + 1
            plus = plus * 10 + 1
        
        init = cur

        while True:
            if cur > high:
                break
            if cur >= low:
                ans.append(cur)
            if cur % 10 == 9:
                l = init % 10
                init = init * 10 + l + 1
                cur = init
                plus = plus * 10 + 1
            else:
                cur = cur + plus
            
        return ans
