"""
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        math_items = {'+', '-', '*', '/'}
        for item in tokens:
            if item in math_items:
                first = stack.pop()
                second = stack.pop()
                res = int(eval(f'{second} {item} {first}'))
                stack.append(res)
            else:
                stack.append(item)
        return int(stack.pop())
