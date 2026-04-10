# Problem: #2069 - Walking Robot Simulation II
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/walking-robot-simulation-ii/
# Submitted: 2026-04-07
class Robot:

    def __init__(self, width: int, height: int):
        self.moved = False
        self.w = width - 1
        self.h = height - 1
        self.direction = ["East", "North", "West", "South"]

        self.modulo = (width - 1) * 2 + (height - 1) * 2
        self.cur = 0

    def step(self, num: int) -> None:
        self.moved = True
        self.cur += num % self.modulo
        self.cur %= self.modulo

    def getPos(self) -> List[int]:
        x = 0
        y = 0
        num = self.cur
        w = self.w
        h = self.h
        x = min(w, num)
        num -= x
        y = min(h, num)
        num -= y
        x -= min(num, w)
        num -= min(num, w)
        y -= min(num, h)
        num -= min(num, h)
        return [x, y]

    def getDir(self) -> str:
        if not self.moved:
            return self.direction[0]
        w = self.w
        h = self.h
        idx = 0
        pos = self.cur
        if self.cur in range(1, w + 1):
            return self.direction[0]
        if self.cur in range(w + 1, w + h + 1):
            return self.direction[1]
        if self.cur in range(w + h + 1, 2 * w + h + 1):
            return self.direction[2]

        return self.direction[3]



# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
