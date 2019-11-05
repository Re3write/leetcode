# 贪心算法，自己解非最优解

tasks = ["A", "A", "A", "B", "B", "B", 'C', 'C', 'D']

n = 3


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict = {}
        for task in tasks:
            if task in dict:
                dict[task] = dict[task] + 1
            else:
                dict[task] = 1
        busy = sorted(dict.items(), key=lambda x: x[1], reverse=False)
        busy = [i[1] for i in busy]
        time = 0
        length = len(busy)
        for index, catgory in enumerate(busy):
            if catgory != 0:
                for i in range(index, length):
                    busy[i] = busy[i] - catgory
                if (length - index) > n:
                    time = time + (catgory * (length - index))
                elif (length - index) <= n:
                    time = time + ((catgory - 1) * (n + 1)) + length - index
        return time


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        length = len(tasks)
        if length <= 1:
            return length

        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)

        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)

        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1

        # 如果结果比任务数量少，则返回总任务数
        return res if res >= length else length

