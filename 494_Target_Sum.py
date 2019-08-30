nums = [1, 1, 1, 1, 1]
S = 3

graph = {}
for index, value in enumerate(nums):
    if index % 2 == 0:
        graph[index] = [index + 2, index + 3]
    elif index % 2 == 1:
        graph[index] = [index + 1, index + 2]

print(graph)
length=len(nums)
if length%2==0:
    graph[length-1]=[]
    graph[length-2]=[]
else:
    graph[length - 1] = []
    graph[length - 2]=[length-1]
    graph[length-3]=[length-1]
print(graph)

count = 0
stack = [(0, [0], -nums[0])]
while stack:
    index, path, total = stack.pop()
    for i in set(graph[index]) - set(path):
        if i % 2 == 0:
            total = total - nums[i // 2]
            stack.append((i, path + [i], total))
        elif i % 2 == 1:
            total = total + nums[i // 2]
        stack.append((i, path + [i], total))
        if total == S:
            count += 1
stack.clear()

stack = [(1, [1], nums[0])]
while stack:
    index, path, total = stack.pop()
    for i in set(graph[index]) - set(path):
        if i % 2 == 0:
            total = total - nums[i // 2]
            stack.append((i, path + [i], total))
        elif i % 2 == 1:
            total = total + nums[i // 2]
        stack.append((i, path + [i], total))
        if total == S:
            count += 1
print(count)

# a=[1,2]
# b=[1,3,4]
# for i in set(a)-set(b):
#     print(i)
