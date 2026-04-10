# Problem: #874 - Walking Robot Simulation
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/walking-robot-simulation/
# Submitted: 2026-04-06
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        idxdir = 0
        pos = [0, 0]
        obs = {tuple(x) for x in obstacles}
        for command in commands:
            if command == -1:
                idxdir = (idxdir + 1) % 4
            elif command == -2:
                idxdir = (idxdir - 1) % 4
            else:
                d = direction[idxdir]
                end = [pos[0] + d[0] * command, pos[1] + d[1] * command]

                for i in range(command):
                    x, y = pos[0] + d[0], pos[1] + d[1]
                    if (x, y) in obs:
                        break
                    pos = [x, y]

                ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
        
        return ans
