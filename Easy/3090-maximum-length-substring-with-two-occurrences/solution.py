# Problem: #3090 - Maximum Length Substring With Two Occurrences
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
# Submitted: 2026-08-14
# Tags: Hash Table, String, Sliding Window
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        k = 2
        l = 0
        r = 0
        cnt = {}
        cnt[s[0]] = 1
        ans = 1
        max_freq = [1]
        n = len(s)
        
        while r < n:
            max_val = max_freq[-1]
            if max_val <= k:
                ans = max(ans, r - l + 1)
                r += 1
                if r >= n:
                    break
                cnt[s[r]] = cnt.get(s[r], 0) + 1
                if cnt[s[r]] >= max_val:
                    max_freq.append(cnt[s[r]])
            else:
                if cnt[s[l]] == max_val:
                    max_freq.pop()
                cnt[s[l]] -= 1
                l += 1

        return ans
        
