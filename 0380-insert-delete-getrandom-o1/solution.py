# Problem: #380 - Insert Delete GetRandom O(1)
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/insert-delete-getrandom-o1/
# Submitted: 2026-04-10
class RandomizedSet:

    def __init__(self):
        self.val_idx = {}
        self.col =  set()
        self.l = []

    def insert(self, val: int) -> bool:
        col = self.col
        if val in col:
            return False
        else:
            col.add(val)
            self.l.append(val)
            self.val_idx[val] = len(self.l) - 1
            return True

    def remove(self, val: int) -> bool:
        col = self.col
        m = self.val_idx
        l = self.l
        if val in col:
            col.remove(val)
            if l[-1] != val:
                index = m[val]
                swap = l[-1]
                l[index], l[-1] = l[-1], l[index]
                m[swap] = index
                
            l.pop()
            m.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
