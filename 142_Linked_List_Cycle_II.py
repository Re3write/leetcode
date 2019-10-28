# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None or head.next.next == None:
            return None
        slow, fast = head.next, head.next.next
        while (slow != fast):
            if fast == None or slow == None or slow.next == None or fast.next == None:
                return None
            slow = slow.next
            fast = fast.next.next

        while (head != slow):
            head = head.next
            slow = slow.next

        return slow