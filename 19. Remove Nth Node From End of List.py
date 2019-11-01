# 先全部存下来

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        Node_List = []
        root = head
        while root:
            Node_List.append(root)
            root = root.next
        length = len(Node_List)
        if length == 1:
            return None
        index_pre =  length -1 - n
        index_next = length + 1 - n
        if index_pre < 0:
            head = Node_List[index_next]
        elif index_next >= length:
            Node_List[index_pre].next = None
        else:
            Node_List[index_pre].next = Node_List[index_next]
        return head


#双指针
#设置一个虚拟节点指向头结点
# 上述算法可以优化为只使用一次遍历。我们可以使用两个指针而不是一个指针。第一个指针从列表的开头向前移动 n+1n+1 步，而第二个指针将从列表的开头出发。现在，这两个指针被 nn 个结点分开。
# 我们通过同时移动两个指针向前来保持这个恒定的间隔，直到第一个指针到达最后一个结点。此时第二个指针将指向从最后一个结点数起的第 nn 个结点。我们重新链接第二个指针所引用的结点的 next 指针指向该结点的下下个结点。

# 思路
# 这里只针对第二个一次遍历的方法
# 用一个快指针，一个慢指针
# 快指针和慢指针先从头节点开始隔开N个距离
# 两个指针一起遍历，到快指针到尾巴为止
# 此时头指针是要删除的节点
# 为什么需要哑节点？因为如果没有哑结点的话，对于整个链表为空的情况就会很难处理。比如说，链表只有一个结点，并且需要删除这个节点。如果只有head，是很难处理的。如果设置了dummy.next = head，就可以设置dummy.next = None同时返回dummy.next
# 代码


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast,slow = dummy,dummy
        for  i in range(n+1):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
