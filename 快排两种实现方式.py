#经典写法

def quickSort(list, start, end):
    if start>end:
        return
    i, j = start, end
    flag = list[start]
    while True:
        #先从右往左找
        while j>i and list[j] >= flag:
            j = j - 1

        #再从左往右找
        while i< j and list[i] <= flag:
            i += 1

        if i < j:
            list[i], list[j] = list[j], list[i]
        elif i == j:
            #当左右相等时第一次递归结束
            list[start], list[i] = list[i], list[start]
            break
    quickSort(list,start, i-1)
    quickSort(list, i+1, end)


#快速写法

def quicksort(list):
    if len(list) <= 1:
        return list

    p = list[0]
    left = quicksort([i for i in list[1:] if i < p])
    right = quicksort([i for i in list[1:] if i >= p])
    return left + [p] + right