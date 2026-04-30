# Problem: #224 - Basic Calculator
# Difficulty: Hard
# Language: Python3
# URL: https://leetcode.com/problems/basic-calculator/
# Submitted: 2026-04-30
# Tags: Math, String, Stack, Recursion
class Solution:
    def calculate(self, s: str) -> int:
        def st(arr):
            ans = int(arr[0])
            i = 1
            while i < len(arr):
                if arr[i] == "-":
                    ans -= int(arr[i + 1])
                elif arr[i] == "+":
                    ans += int(arr[i + 1])
                i += 2
            return str(ans)

        def calc(target, idx, arr):
            n = len(target)
            while idx < n:
                ch = target[idx]
                if ch == "(":
                    val, idx = calc(target, idx + 1, [])
                    arr.append(val)
                elif ch == ")":
                    return st(arr), idx + 1
                elif ch.isdigit():
                    if arr and arr[-1][-1].isdigit():
                        arr.append(arr.pop() + ch)
                    else:
                        arr.append(ch)
                    idx += 1
                elif ch in "+-":
                    if not arr:              
                        arr.append("0")
                    arr.append(ch)
                    idx += 1
                else:                         
                    idx += 1
            return st(arr), idx

        result, _ = calc(s, 0, [])
        return int(result)
