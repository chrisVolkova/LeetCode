"""
Link: https://leetcode.com/problems/reorder-list/description/

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return head

        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        cur_head = slow.next
        prev = slow
        while cur_head:
            tmp = cur_head.next
            cur_head.next = prev
            prev = cur_head
            cur_head = tmp
        slow.next = None

        cur_head = head
        while cur_head and prev:
            tmp = cur_head.next
            cur_head.next = prev
            tmp2 = prev.next
            prev.next = tmp
            prev = tmp2
            cur_head = tmp

        return head
    