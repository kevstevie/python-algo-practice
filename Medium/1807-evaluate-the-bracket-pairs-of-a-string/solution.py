# Problem: #1807 - Evaluate the Bracket Pairs of a String
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
# Submitted: 2026-09-26
# Tags: Array, Hash Table, String
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ans = ""
        temp = ""
        flag = False
        dic = {}
        qes = "?"

        for i in knowledge:
            dic[i[0]] = i[1]

        for i in s:
            if i == ')':
                if temp in dic:
                    ans += dic[temp]
                else:
                    ans += qes
                temp = ""
                flag = False
                continue
            if i == '(':
                flag = True
                continue
            if not flag:
                ans += i
            if flag:
                temp += i

        return ans
