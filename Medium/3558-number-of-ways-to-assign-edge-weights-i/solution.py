# Problem: #3558 - Number of Ways to Assign Edge Weights I
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/
# Submitted: 2026-06-11
# Tags: Math, Tree, Depth-First Search
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        depth = 0
        visited = [False] * (n + 1)
        visited[1] = True
        q = [(1, 0)]
        while q:
            node, d = q.pop()
            depth = max(depth, d)
            for nxt in g[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, d + 1))

        return pow(2, depth - 1, MOD)
