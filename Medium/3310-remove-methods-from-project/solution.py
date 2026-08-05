# Problem: #3310 - Remove Methods From Project
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/remove-methods-from-project/
# Submitted: 2026-08-05
# Tags: Depth-First Search, Breadth-First Search, Graph Theory
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]          
        for a, b in invocations:
            g[a].append(b)

        st = [k]
        v = [False] * n                     
        v[k] = True

        while st:
            cur = st.pop()
            for nxt in g[cur]:
                if not v[nxt]:
                    v[nxt] = True
                    st.append(nxt)

        for a, b in invocations:            
            if not v[a] and v[b]:
                return list(range(n))

        return [i for i in range(n) if not v[i]]
