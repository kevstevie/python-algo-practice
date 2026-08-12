# Problem: #2958 - Length of Longest Subarray With at Most K Frequency
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
# Submitted: 2026-08-12
# Tags: Array, Hash Table, Sliding Window
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        cnt = {}
        cnt[nums[0]] = 1
        ans = 1
        max_freq = [1]
        n = len(nums)
        
        while r < n:
            max_val = max_freq[-1]
            if max_val <= k:
                ans = max(ans, r - l + 1)
                r += 1
                if r >= n:
                    break
                cnt[nums[r]] = cnt.get(nums[r], 0) + 1
                if cnt[nums[r]] >= max_val:
                    max_freq.append(cnt[nums[r]])
            else:
                if cnt[nums[l]] == max_val:
                    max_freq.pop()
                cnt[nums[l]] -= 1
                l += 1

        return ans
        
