class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
         result = []
         candidates = sorted(candidates)
         if not candidates:
             return []
         def dfs(sums,temp):
             if sums == 0:
                 if not result or sorted(temp) not in result:
                    result.append(temp[:])
             for num in candidates:
                 if sums - num >= 0:
                    temp.append(num)
                    dfs(sums-num,temp)
                    temp.pop(-1)
         dfs(target,[])
         return result


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if(not candidates):
            return []
        n=len(candidates)
        res=[]
        candidates.sort()
        def helper(i,tmp,target):
            if(target==0):
                res.append(tmp)
                return
            if(i==n or target<candidates[i]):
                return
            helper(i,tmp+[candidates[i]],target-candidates[i])
            helper(i+1,tmp,target)
        helper(0,[],target)
        return res
