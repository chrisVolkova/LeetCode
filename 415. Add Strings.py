"""
Link: https://leetcode.com/problems/add-strings/description/

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must
also not convert the inputs to integers directly.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        short, long = num1, num2
        if len(num1) > len(num2):
            short, long = num2, num1
        mod = 0
        res = []
        first, second = len(short) - 1, len(long) - 1

        while first >= 0 and second >= 0:
            cnt_res = int(short[first]) + int(long[second]) + mod
            res.append(cnt_res % 10)
            mod = cnt_res // 10
            first -= 1
            second -= 1

        while second >= 0:
            cnt_res = int(long[second]) + mod
            res.append(cnt_res % 10)
            mod = cnt_res // 10
            second -=1

        if mod != 0:
            res.append(mod)
        res.reverse()
        return ''.join(map(str, res))
