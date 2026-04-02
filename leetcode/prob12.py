from collections import deque


class Solution:
    def intToRoman(self, num: int) -> str:
        w = [["I", "V"], ["X", "L"], ["C", "D"], ["M"]]

        ans = deque()
        idx = 0

        while num > 0:
            targ = num % 10
            temp = ""
            if targ == 9:
                temp = w[idx][0] + w[idx + 1][0]
            elif targ == 4:
                temp = w[idx][0] + w[idx][1]

            else:
                if targ >= 5:
                    temp = w[idx][1]
                    targ -= 5

                temp = temp + w[idx][0] * targ

            ans.appendleft(temp)

            idx += 1
            num //= 10

        return "".join(ans)
