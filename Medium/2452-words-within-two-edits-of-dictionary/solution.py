# Problem: #2452 - Words Within Two Edits of Dictionary
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/words-within-two-edits-of-dictionary/
# Submitted: 2026-04-22
# Tags: Array, String, Trie
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for s1 in queries:
            for s2 in dictionary:
                if len(s1) != len(s2):
                    continue
                dif = 0
                for i in range(len(s1)):
                    if s1[i] != s2[i]:
                        dif += 1
                if dif <= 2:
                    ans.append(s1)
                    break

        return ans
