"""
Link: https://leetcode.com/problems/remove-linked-list-elements/description/

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
and return the new head.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        cur_head = head
        while cur_head:
            if cur_head.val == val:
                prev.next = cur_head.next
            else:
                prev = cur_head
            cur_head = cur_head.next

        return dummy.next
    