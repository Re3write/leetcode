nums = [1, 1, 1, 1, 1]
S = 3

graph = {}
for index in range(2*len(nums)):
    if index % 2 == 0:
        graph[index] = [index + 2, index + 3]
    elif index % 2 == 1:
        graph[index] = [index + 1, index + 2]


graph[2*len(nums)-1]=[]
graph[2*len(nums)-2]=[]
print(graph)

count = 0
stack = [(0, [0], -nums[0])]
while stack:
    index, path, total = stack.pop()
    print(index,path,total)
    for i in set(graph[index]) - set(path):
        print(set(graph[index]) - set(path))
        print(i)
        if i % 2 == 0:
            total = total - nums[i // 2]
            stack.append((i, path + [i], total))
        elif i % 2 == 1:
            total = total + nums[i // 2]
            stack.append((i, path + [i], total))
        if total == S:
            count += 1
# stack.clear()
#
# stack = [(1, [1], nums[0])]
# while stack:
#     index, path, total = stack.pop()
#     for i in set(graph[index]) - set(path):
#         if i % 2 == 0:
#             total = total - nums[i // 2]
#             stack.append((i, path + [i], total))
#         elif i % 2 == 1:
#             total = total + nums[i // 2]
#             stack.append((i, path + [i], total))
#         if total == S:
#             count += 1
print(count)

# a=[1,2]
# b=[1,3,4]
# for i in set(a)-set(b):
#     print(i)
