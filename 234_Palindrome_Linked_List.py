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



#快慢指针 翻转链表
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 预处理
        if head == None or head.next == None:
            return True
        recnct,slow,fast = head,head,head
        newhead = None
        # 遍历链表
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow
            slow = slow.next
            # 反转链表（前半部分）
            tmp.next = newhead
            newhead = tmp
        # 连接中间断裂的链表
        recnct.next = slow
        ps = newhead
        #判断链长为奇为偶？
        pf = slow.next if fast else slow
        # 遍历前半部分、后半部分链表，判断对应值是否相等？
        while pf:
            if ps.val != pf.val:
                return False
            ps = ps.next
            pf = pf.next
        return True

