# 首先要求时间复杂度小于O(N^2)，所以能想到用hash（O(1)）或排序（O(NlogN)），但是这两种不满足空间复杂度为O(1)且不修改原数组
#
# 其次看能否通过异或来查找，因为一个数异或自己等于0：i^i=0，并且异或具有交换律和集合率。所以如果一个数出现2次，而其他数都只出现一次，可以通过1到n的异或值和这个列表每个值异或，那么最终结果值就是重复的数字（因为其他数组都出现2次，而重复的那个数字出现3次）。但是本题重复数字可能出现多次。
#
# 然后苦想其他办法，O(NlogN)，数字一定在[1, n]区间，且一定有一个重复数字。那么联想，一定有一半不正常，如果每次能排除一半，这种折半的思想就是logN。二分查找
#
# 然后再想其他更优化的办法O(N)。n+1个数字，在区间[1,n]。那么一定有两个数字一样（鸽巢理论能证明）。即：0到n个下标，即key，值为1到n。那么一定2个下标对应的值一样，如果把值看做next指针，即值为其后继节点，那么一定有2个节点都指到了同一个节点。这样的问题就跟链表里是否有环一样了，有环就是两个节点指到了同一个节点。（这一点真他妈难想到，可以画图想到）
#
# 那么就转换为两种解题办法：
#
#
# 本题可用二分查找，整个算法时间复杂度为 O(NlogN)，由题意可知搜索范围在 1 到 n 之间，那么如何缩小范围？
# 只需判断数组中不超过中间数 m 的元素数量是否大于 m 即可，若大于，则表示范围 1 到 m 内肯定包含重复的数字
# 搜索范围为 [1, n]，向左（包括target）搜索的条件为：不大于 n 的数字在 nums 存在超过 m 个，即搜索范围可以被缩小为 [1, m]

#十分好用的二分法模板
# https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
#二分查找
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1
            counter = 0
            for num in nums:
                if num <= mid:
                    counter += 1

            # 【注意】如果小于等于 mid 的个数如果多于 mid，例如：
            # 8 个萝卜 放在 7 个坑里，就至少有 1 个坑里至少有 2 个萝卜
            # 这个坑的位置可能是 1、2、3、4、5、6、7
            # 重复的数就一定在 [1, mid] 里面，包括 1 和 mid
            # 此时，不排除中位数的分支逻辑好想，因此写在前面

            if counter > mid:
                right = mid
            else:
                # 我认为这个逻辑太难想了，但我知道这样写一定对
                left = mid + 1

        return left




#链表找环的开始


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 此题转换为链表找环的开始位置，前提条件告诉我们是一定有环
        # 根据floyd判圈办法，一个快指针一个慢指针，二者一定在环上相遇，设相遇点为M点，
        # 快是慢的速度的2倍，时间相同，设慢的距离为s，那么快的距离为2s
        # m为链表头距离环开始位置的距离，k为环开始位置到M点的距离, N为环长度
        # s = m + a*N +k, 2s = m + b*N +k，二者相减，s = (a-b)*N
        # 由此可见，慢指针走过的距离是环长的整数倍，即链表头到M点是环长的整数倍
        # 如果是1倍的话，把m截距离旋转到环上，跟环融合，那么链表头一定落在M点，
        # 即fast和slow都落在M点，那么二者到环开始位置距离相同，必然在此处相遇。
        # 如果是N倍（N>1）时，只不过slow指针多转几圈而已，后二者扔在此处相遇
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]  # next
            fast = nums[nums[fast]]  # next.next
            if slow == fast:
                break


        # slow和fast会在环中相遇，假设一些量：起点到环的入口长度为m，环的周长为c，
        # 在fast和slow相遇时slow走了n步，fast走了2n步，fast比slow多走了n步，而这n步全用在了在环里循环。
        # Find the "entrance" to the cycle.以下，入口就是重复数字
        # fast和slow相遇时，slow在环中行进的距离是n - m，其中n % c == 0。这时我们让再让slow前进m步——也就是在环中走了n步了。
        # 而n % c == 0
        # 即slow在环里面走的距离是环的周长的整数倍，就回到了环的入口了，而入口就是重复的数字。
        # 我们不知道起点到入口的长度m，所以弄个finder和slow一起走，他们必定会在入口处相遇。


        fast = nums[0]
        while True:
            if slow == fast:
                break
            slow = nums[slow]
            fast = nums[fast]

        return slow

