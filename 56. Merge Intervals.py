class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x : x[0])
        result = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i,inter in enumerate(intervals[1:]):
            if inter[0]>=start and inter[0] <= end and inter[1] >= end:
                end = inter[1]
            elif inter[0] >= start and inter[1] <= end:
                end = end
            else:
                result.append([start,end])
                if i + 1 < len(intervals):
                   start = intervals[i+1][0]
                   end = intervals[i+1][1]
        result.append([start,end])
        return result