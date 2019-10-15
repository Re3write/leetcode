# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        li = []
        root = head
        while head:
            li.append(head)
            head = head.next
        if len(li) == 1:
            return root

        li = sorted(li, key=lambda x: x.val)
        for i in range(len(li)):
            li[i].next = None

        for i in range(len(li) - 1):
            li[i].next = li[i + 1]

        return li[0]






#归并排序

    class Solution:
        def sortList(self, head: ListNode) -> ListNode:
            if not head or not head.next:
                return head
            slow, fast = head, head.next
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            mid, slow.next = slow.next, None
            left, right = self.sortList(head), self.sortList(mid)

            res = h = ListNode(0)
            while left and right:
                if left.val < right.val:
                    h.next, left = left, left.next
                else:
                    h.next, right = right, right.next
                h = h.next
            h.next = left if left else right
            return res.next

