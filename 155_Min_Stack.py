# 解题思路：
# 借用一个辅助栈min_stack，用于存获取stack中最小值。
#
# 算法流程：
#
# push()方法： 每当push()新值进来时，如果 小于等于 min_stack栈顶值，则一起push()到min_stack，即更新了栈顶最小值；
# pop()方法： 判断将pop()出去的元素值是否是min_stack栈顶元素值（即最小值），如果是则将min_stack栈顶元素一起pop()，这样可以保证min_stack栈顶元素始终是stack中的最小值。
# getMin()方法： 返回min_stack栈顶即可。
# min_stack作用分析：
#
# min_stack等价于遍历stack所有元素，把升序的数字都删除掉，留下一个从栈底到栈顶降序的栈。
# 相当于给stack中的降序元素做了标记，每当pop()这些降序元素，min_stack会将相应的栈顶元素pop()出去，保证其栈顶元素始终是stack中的最小元素。
# 复杂度分析：
#
# 时间复杂度 O(1)O(1) ：压栈，出栈，获取最小值的时间复杂度都为 O(1)O(1) 。
# 空间复杂度 O(N)O(N) ：包含 NN 个元素辅助栈占用线性大小的额外空间。

class MinStack:

    # 辅助栈和数据栈同步
    # 思路简单不容易出错

    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):   #每次压入数据，helper同步压入目前数组的最小值
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        if self.data:
            self.helper.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]
