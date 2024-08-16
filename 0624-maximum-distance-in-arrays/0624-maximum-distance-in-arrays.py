class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        a=arrays[0][0]
        b=arrays[0][-1]
        res=0
        for i in arrays[1:]:
            res=max(res,abs(i[-1]-a),abs(b-i[0]))
            b=max(i[-1],b)
            a=min(i[0],a)
        return res