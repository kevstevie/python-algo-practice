# Problem: #1722 - Minimize Hamming Distance After Swap Operations
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
# Submitted: 2026-04-21
# Tags: Array, Depth-First Search, Union-Find
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        arr = [i for i in range(n)]
        cnt = {}

        def find(a):
            if arr[a] == a:
                return a
            arr[a] = find(arr[a])
            return arr[a]
        
        def union(a, b):
            x = find(a)
            y = find(b)
            if x >= y:
                arr[x] = y
            else:
                arr[y] = x
        
        for (i, j) in allowedSwaps:
            union(i, j)
            
        for i in range(n):
            root = find(i)
            cnt[root] = cnt.get(root, {})
            cnt[root][source[i]] = cnt[root].get(source[i], 0) + 1

        ans = 0

        for i in range(n):
            root = find(i)
            if cnt[root].get(target[i], 0) > 0:
                cnt[root][target[i]] -= 1
            else:
                ans += 1

        return ans
