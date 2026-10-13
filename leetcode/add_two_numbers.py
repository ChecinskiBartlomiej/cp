#https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        l3_head = ListNode()
        l3_current = l3_head
        c = 0

        while (l1 is not None) or (l2 is not None) or (c != 0):

            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            
            s = x + y + c
            d = s % 10
            c = s // 10

            l3_current.next = ListNode(d)
            l3_current = l3_current.next


            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return l3_head.next