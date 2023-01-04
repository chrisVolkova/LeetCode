"""
Link: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur_head = head
        mod = 0
        while l1 and l2:
            cur_val = l1.val + l2.val + mod
            mod = cur_val // 10
            cur_head.next = ListNode(val=cur_val % 10)
            cur_head, l1, l2 = cur_head.next, l1.next, l2.next

        if l1 or l2:
            long = l1 if l1 else l2
            while long:
                cur_val = long.val + mod
                mod = cur_val // 10
                cur_head.next = ListNode(val=cur_val % 10)
                cur_head, long = cur_head.next, long.next
        if mod > 0:
            cur_head.next = ListNode(mod)

        return head.next
    