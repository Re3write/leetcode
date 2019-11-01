# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        dummy = new_head = ListNode(10)
        while l1 and l2:
            if l1.val <= l2.val:
                new_head.next = l1
                l1 = l1.next
            else:
                new_head.next = l2
                l2 = l2.next

            new_head = new_head.next

        if l1 == None:
            new_head.next = l2
        elif l2 == None:
            new_head.next = l1

        return dummy.next