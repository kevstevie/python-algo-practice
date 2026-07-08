# Problem: #3756 - Concatenate Non-Zero Digits and Multiply by Sum II
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/
# Submitted: 2026-07-08
# Tags: Math, String, Prefix Sum
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        mod = 10 ** 9 + 7

        cnt = [0] * (n + 1)    
        sums = [0] * (n + 1)   
        val = [0] * (n + 1)
        pow10 = [1] * (n + 1)  

        for i in range(1, n + 1):
            d = int(s[i - 1])
            pow10[i] = pow10[i - 1] * 10 % mod
            if d != 0:
                cnt[i] = cnt[i - 1] + 1
                sums[i] = (sums[i - 1] + d) % mod
                val[i] = (val[i - 1] * 10 + d) % mod
            else:
                cnt[i] = cnt[i - 1]
                sums[i] = sums[i - 1]
                val[i] = val[i - 1]

        ans = []
        for start, end in queries:
            ssum = (sums[end + 1] - sums[start]) % mod
            if ssum == 0:
                ans.append(0)
                continue
            k = cnt[end + 1] - cnt[start]
            num = (val[end + 1] - val[start] * pow10[k]) % mod
            ans.append(num * ssum % mod)
        return ans
