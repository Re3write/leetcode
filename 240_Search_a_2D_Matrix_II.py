matrix = [[-1]]
target = -1

i = len(matrix) - 1
j = 0

#左下角或者右上角排除法查找
# while i >= 0 and j <= len(matrix[0]) - 1:
#     if target < matrix[i][j]:
#         i -= 1
#     elif target > matrix[i][j]:
#         j += 1
#     elif target == matrix[i][j]:
#         return True
# return False


#二分法
for i in range(len(matrix)):
    left = 0
    right = len(matrix[0]) - 1
    while left <= right:
        mid = left + (right - left) // 2
        print(mid)
        if target == matrix[i][mid]:
            print('true')
        if left == right:
            break
        elif target < matrix[i][mid]:
            right = mid
        elif target > matrix[i][mid]:
            left = mid + 1

print('false')

# for i in matrix:
#     if target in i:
#         return True
# return False