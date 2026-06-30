# Problem: #1358 - Number of Substrings Containing All Three Characters
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# Submitted: 2026-06-30
# Tags: Hash Table, String, Sliding Window
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        cnts = [0] * 3
        n = len(s)
        l = 0
        r = 0
        cnts[ord(s[0]) - ord('a')] += 1

        while r < n:
            if cnts[0] >= 1 and cnts[1] >= 1 and cnts[2] >= 1:
                ans += n - r
                al = ord(s[l]) - ord('a')
                cnts[al] -= 1
                l += 1
            else:
                r += 1
                if r == n:
                    continue
                al = ord(s[r]) - ord('a')
                cnts[al] += 1

        return ans
