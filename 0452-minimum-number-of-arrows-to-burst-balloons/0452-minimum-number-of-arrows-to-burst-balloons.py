class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        p.sort(key=lambda x:x[1])
        c=1
        end=p[0][1]
        for i in range(1,len(p)):
            if p[i][0]>end:
                c+=1            
                end=p[i][1]
        return c