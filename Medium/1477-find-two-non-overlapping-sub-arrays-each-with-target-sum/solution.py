# Problem: #1477 - Find Two Non-overlapping Sub-arrays Each With Target Sum
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
# Submitted: 2026-09-17
# Tags: Array, Hash Table, Binary Search, Dynamic Programming, Sliding Window
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        l = 0
        r = 0
        tot = arr[0]
        INF = float('inf')
        dp = [INF] * n
        ans = INF

        while r < n:
            rf = False
            lf = False
            if tot == target:
                prev = dp[r - 1] if r > 0 else INF
                dp[r] = min(prev, r - l + 1)
                if l > 0 and dp[l - 1] != INF:
                    ans = min(ans, dp[l - 1] + r - l + 1)
                rf = True
            elif tot < target:
                dp[r] = dp[r - 1] if r > 0 else INF
                rf = True
            elif tot > target:
                dp[r] = dp[r - 1] if r > 0 else INF
                if l == r:
                    rf = True
                    lf = True
                else:
                    lf = True
            if rf:
                r += 1
                if r >= n:
                    break
                tot += arr[r]
            if lf:
                tot -= arr[l]
                l += 1
        
        ans = -1 if ans == INF else ans
        return ans
