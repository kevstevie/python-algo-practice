class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n != 1:
            n = self.recur(n)
            if n in s:
                return False
            else:
                s.add(n)

        return True

    def recur(self, num: int) -> int:
        if num == 0:
            return 0
        mul = num % 10

        return mul ** 2 + self.recur(num // 10)
