#栈计数

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        result = [0 for _ in range(length)]

        flag = 1
        today = 0
        for x in range(length):
            today = T[x]
            flag = 1
            for y in T[x + 1:]:
                if y <= today:
                    flag = flag + 1
                elif y > today:
                    result[x] = flag
                    break

        return result

#同样方法python3不过，java可以过


class Solution(object):
    def dailyTemperatures(self, T):
        stack, r = [], [0] * len(T)
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t: r[stack.pop()] = i - stack[-1]
            stack.append(i)
        return r


# 维护递减栈，后入栈的元素总比栈顶元素小。
#
# 比对当前元素与栈顶元素的大小
# 若当前元素 < 栈顶元素：入栈
# 若当前元素 > 栈顶元素：弹出栈顶元素，记录两者下标差值即为所求天数
# 这里用栈记录的是
# T
# 的下标。

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = list()
        t_length = len(T)
        res_list = [0 for _ in range(t_length)]

        for key, value in enumerate(T):
            if stack:
                while stack and T[stack[-1]] < value:
                    res_list[stack[-1]] = key - stack[-1]
                    stack.pop()
            stack.append(key)
        return res_list



