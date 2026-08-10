# Problem: #1510 - Stone Game IV
# Difficulty: Hard
# Language: Python3
# URL: https://leetcode.com/problems/stone-game-iv/
# Submitted: 2026-08-10
# Tags: Math, Dynamic Programming, Minimax, Game Theory, Nim Game, Sprague–Grundy Theorem, Zero-Sum Game
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            k = math.isqrt(i)
            for j in range(1, k + 1):
                if not dp[i - j * j]:
                    dp[i] = True

        return dp[n]
