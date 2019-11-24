#超时，first版本

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        def find_all(s,tmp,result):
            if not s:
                return result.add(tmp[:])
            for i in range(len(s)):
                find_all(s[:i]+s[i+1:],tmp+s[i],result)

        final = {}
        flag = 0
        for s in strs:
            for a in final.keys():
                if s in a:
                    flag = 1
                    final[a].append(s)
            if flag == 0:
                result = set()
                find_all(s,'',result)
                final[tuple(result)] = [s]
            flag = 0

        return [x for x in final.values()]

#second版本
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            dic[tuple(sorted(s))] = dic.get(tuple(sorted(s)), []) + [s]
        return dic.values()