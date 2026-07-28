# Problem: #3517 - Smallest Palindromic Rearrangement I
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/smallest-palindromic-rearrangement-i/
# Submitted: 2026-07-28
# Tags: String, Sorting, Counting Sort
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        ans = ''

        odd = []
        for i in range(26):
            word = chr(ord('a') + i)
            if arr[i] == 0:
                continue
            target = arr[i] // 2
            if arr[i] % 2 == 1:
                odd.append(word)
            ans += word * target
        rev = ans[::-1]
        if odd:
            ans += odd[0]
        ans += rev
        
        return ans
