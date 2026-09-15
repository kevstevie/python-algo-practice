# Problem: #205 - Isomorphic Strings
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/isomorphic-strings/
# Submitted: 2026-09-15
# Tags: Hash Table, String
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        col = set()

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c2 in col:
                if c1 not in m:
                    return False
                if m[c1] != c2:
                    return False
            else:
                if c1 in m:
                    return False
                m[c1] = c2
                col.add(c2)
        return True
