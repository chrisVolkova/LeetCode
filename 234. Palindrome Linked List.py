"""
Link: https://leetcode.com/problems/palindrome-linked-list/description/

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next

        left, right = 0, len(res) - 1
        while left < right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1

        return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = slow
        cur_head = slow.next
        while cur_head:
            tmp = cur_head.next
            cur_head.next = prev
            prev = cur_head
            cur_head = tmp
        slow.next = None

        left, right = head, prev
        while left and right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True
