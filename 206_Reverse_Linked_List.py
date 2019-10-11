
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        pre = None
        headnext = head.next
        while True:
            head.next = pre
            pre = head
            if headnext:
                head = headnext
                headnext = headnext.next
            else:
                break
        return head


# 遍历链表，在遍历的过程中更新两个指针pre, head：
# pre, head分别指向前一个节点和当前节点，每次执行head.next = pre
# nex用于提前保存下一个节点。
# 由于需要返回新的链表头部，所以设置跳出条件为head.next == null,跳出后将最后head指向pre，并返回head。
# pythonjava
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return
        pre = None
        while head.next:
            nex = head.next
            head.next = pre
            pre = head
            head = nex
        head.next = pre   #精髓，最终因为null，需要重新连一下
        return head



#多元赋值逆转链表 python多元赋值 在赋值过程中右边的值不会变化，因为在赋值前提前做好了计算
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, rev = head, None   #p 是 维护的next  rev是从头开始的head
        while p:
            rev, rev.next, p = p, rev, p.next
        return rev


# 递归解法
# 解法2 递归
# 最开始 1 -> 2 -> 3 -> 4
# 对于head.next.next = head , 当head在 3 时，相当于加了一个4 -> 3 ，形成回环, 即 1 -> 2 -> 3 <-> 4
# 然后 head.next = None, 取消回环，消除了 3 -> 4
# 1 -> 2 -> 3 <- 4
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        start = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return start


