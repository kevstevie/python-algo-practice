# Problem: #3043 - Find the Length of the Longest Common Prefix
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
# Submitted: 2026-05-21
# Tags: Array, Hash Table, String, Trie
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = Trie()

        for i in arr1:
            root.add(i)
        
        ans = 0

        for i in arr2:
            d = root.find(i)
            ans = max(d, ans)

        return ans

class Trie:
    def __init__(self):
        self.root = Node(-1)

    def add(self, a):
        x = str(a)
        cur = self.root
        for ch in x:
            n = int(ch)
            if not cur.c[n]:
                cur.c[n] = Node(n, cur.d + 1)
            cur = cur.c[n]

    def find(self, a):
        x = str(a)
        cur = self.root
        for ch in x:
            n = int(ch)
            if not cur.c[n]:
                return cur.d
            else:
                cur = cur.c[n]
        return cur.d

class Node:
    def __init__(self, v, d = 0):
        self.c = [None] * 10
        self.v = v
        self.d = d
