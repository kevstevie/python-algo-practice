# Problem: #3014 - Minimum Number of Pushes to Type Word I
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/
# Submitted: 2026-07-30
# Tags: Math, String, Greedy
class Solution:
    def minimumPushes(self, word: str) -> int:
        dic = {}
        for c in word:
            dic[c] = dic.get(c, 0) + 1
        
        l = sorted(list(dic.values()))

        cnt = 0
        ans = 0

        for i in l:
            ans += i * (cnt // 8 + 1)
            cnt += 1

        return ans
