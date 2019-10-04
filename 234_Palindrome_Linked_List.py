class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
         numbers = []
         while(head!=None):
                numbers.append(head.val)
                head = head.next
         length = len(numbers)
         if length < 2:
                return True
         if length%2 ==0:
            if numbers[:length//2] == numbers[length//2:][::-1]:
               return True
            else:
                return False
         else:
            if numbers[:length//2+1] == numbers[length//2:][::-1]:
                return True
            else:
                return False



#快慢指针 翻转链表设置快慢指针
# 每次快指针增加两个，慢指针增加一个
# 这样当快指针结尾时，慢指针指向了链表的中间
# 用慢指针逆序链表的后半部分，利用Python交换的特性，不需要额外的tmp结点
# 一个从头开始，一个从中间开始，判断两者是否相同

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow,fast,prev = head,head,None
        while fast is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else fast.next
        while slow is not None:
            slow.next, slow, prev= prev, slow.next, slow
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
