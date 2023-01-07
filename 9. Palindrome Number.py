"""
Link: https://leetcode.com/problems/palindrome-number/description/

Given an integer x, return true if x is a palindrome, and false otherwise.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True

        ans = []
        mod = x
        while mod != 0:
            div = mod % 10
            ans.append(div)
            mod = mod // 10

        left, right = 0, len(ans) - 1
        while left < right:
            if ans[left] != ans[right]:
                return False
            left += 1
            right -= 1
