# Problem: #155 - Min Stack
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/min-stack/
# Submitted: 2026-04-08
class MinStack:

    def __init__(self):
        self.min = []
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min or self.min[-1] >= val:
            self.min.append(val)

    def pop(self) -> None:
        pop = self.st.pop()
        if pop == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]
        else:
            return self.st[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
