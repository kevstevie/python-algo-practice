class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic = {}
        for i in moves:
            dic[i] = dic.get(i, 0) + 1

        return dic.get("U", 0) == dic.get("D", 0) \
        and dic.get("L", 0) == dic.get("R", 0)
