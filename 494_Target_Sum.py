class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if len(nums)==1:
            if nums[0]==S or -nums[0]==S:
               return 1
            else:
               return 0
        graph = {}
        for index in range(2 * len(nums)):
            if index % 2 == 0:
                graph[index] = [index + 2, index + 3]
            elif index % 2 == 1:
                graph[index] = [index + 1, index + 2]

        graph[2 * len(nums) - 1] = []
        graph[2 * len(nums) - 2] = []

        count = 0
        stack = [(0, [0], -nums[0])]
        while stack:
            index, path, total = stack.pop()
            for i in set(graph[index]) - set(path):
                if i % 2 == 0:
                    new_total = total - nums[i // 2]
                    stack.append((i, path + [i], new_total))
                elif i % 2 == 1:
                    new_total = total + nums[i // 2]
                    stack.append((i, path + [i], new_total))
                if new_total == S and len(path + [i]) == len(nums):
                    count += 1
        stack.clear()

        stack = [(1, [1], nums[0])]
        while stack:
            index, path, total = stack.pop()
            for i in set(graph[index]) - set(path):
                if i % 2 == 0:
                    new_total = total - nums[i // 2]
                    stack.append((i, path + [i], new_total))
                elif i % 2 == 1:
                    new_total = total + nums[i // 2]
                    stack.append((i, path + [i], new_total))
                if new_total == S and len(path + [i]) == len(nums):
                    count += 1
        return count