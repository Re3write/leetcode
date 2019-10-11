class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = {}
        for i in prerequisites:
            item = graph.get(i[0], set())
            item.add(i[1])
            graph[i[0]] = item

        root = prerequisites[0][0]
        visit = set()
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop()
            if node in graph:
                visit.add(node)
                for i in graph[node]:
                    if i in visit:
                        return False
                    queue.append(i)
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True

