class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        ans = 0
        oddc = 0
        for c in s:
            m[c] = m.get(c, 0) + 1
            if m[c] % 2 == 0:
                oddc -= 1
                ans += 2
            else:
                oddc += 1

        return ans + (oddc != 0)
