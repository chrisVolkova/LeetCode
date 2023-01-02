"""
Link: https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        
        for char in s:
            if char in brackets:
                if not stack:
                    return False
                cur_char = stack.pop()
                if cur_char != brackets[char]:
                    return False
            else: 
                stack.append(char)

        return not stack
