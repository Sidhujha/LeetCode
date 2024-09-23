class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        c=0
        end=-50001
        for i in intervals:
            if i[0]>=end:
                end=i[1]
            else:
                c+=1
        return c