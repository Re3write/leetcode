#双指针滑动窗口解题
# https://leetcode-cn.com/problems/minimum-window-substring/solution/hua-dong-chuang-kou-suan-fa-tong-yong-si-xiang-by-/string s, t;

#滑动窗口双指针模板
# // 在 s 中寻找 t 的「最小覆盖子串」
# int left = 0, right = 0;
# string res = s;
#
# // 相当于两个计数器
# unordered_map<char, int> window;
# unordered_map<char, int> needs;
# for (char c : t) needs[c]++;
#
# // 记录 window 中已经有多少字符符合要求了
# int match = 0;
#
# while (right < s.size()) {
#     char c1 = s[right];
#     if (needs.count(c1)) {
#         window[c1]++; // 加入 window
#         if (window[c1] == needs[c1])
#             // 字符 c1 的出现次数符合要求了
#             match++;
#     }
#     right++;
#
#     // window 中的字符串已符合 needs 的要求了
#     while (match == needs.size()) {
#         // 更新结果 res
#         res = minLen(res, window);
#         char c2 = s[left];
#         if (needs.count(c2)) {
#             window[c2]--; // 移出 window
#             if (window[c2] < needs[c2])
#                 // 字符 c2 出现次数不再符合要求
#                 match--;
#         }
#         left++;
#     }
# }
# return res;