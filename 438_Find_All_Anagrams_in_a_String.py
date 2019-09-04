s = "cbaebabacd"
p = "abc"



# class Solution:
#     def findAnagrams(self, s: str, p: str) -> list:
#         '''
#         解法1：滑动窗口
#         '''
#         res = []
#         window = {}     # 记录窗口中各个字符数量的字典
#         needs = {}      # 记录目标字符串中各个字符数量的字典
#         for c in p: needs[c] = needs.get(c, 0) + 1  # 统计目标字符串的信息
#
#         length, limit = len(p), len(s)
#         left = right = 0                    # 定理两个指针，分别表示窗口的左、右界限
#
#         while right < limit:
#             c = s[right]
#             if c not in needs:              # 当遇到不需要的字符时
#                 window.clear()              # 将之前统计的信息全部放弃
#                 left = right = right + 1    # 从下一位置开始重新统计
#             else:
#                 window[c] = window.get(c, 0) + 1            # 统计窗口内各种字符出现的次数
#                 if right-left+1 == length:                  # 当窗口大小与目标字符串长度一致时
#                     if window == needs: res.append(left)    # 如果窗口内的各字符数量与目标字符串一致就将left添加到结果中
#
#                     window[s[left]] -= 1                    # 并将移除的字符数量减一
#                     left += 1                               # left右移
#                 right += 1                                  # right右移
#         return res

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length_p = len(p)
        length_s = len(s)
        if length_s < length_p:
            return []

        dict = {}
        dict_find = {}
        for i in p:
            dict[i] = dict.get(i, 0) + 1
        result = []

        for i in range(length_s - length_p + 1):
            substring = s[i:i + length_p]
            for st in substring:
                if st in dict:
                    dict_find[st] = dict_find.get(st, 0) + 1
            if dict == dict_find:
                result.append(i)
            dict_find.clear()
        return result
