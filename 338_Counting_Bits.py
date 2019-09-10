num = 5

res = [0 for _ in range(num + 1)]

res[0] = 0
res[1] = 1
for i in range(2, num + 1):
    if i % 2 == 0:
        res[i] = res[i // 2]
    else:
        res[i] = res[i // 2] + 1

print(res)