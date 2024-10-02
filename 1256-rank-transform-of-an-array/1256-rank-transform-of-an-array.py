class Solution:
    def arrayRankTransform(self, li: List[int]) -> List[int]:
        li1=li[:]
        li1.sort()
        ranks={}
        rank=1
        for i in li1:
            if i not in ranks:
                ranks[i]=rank
                rank+=1
        result=[]
        for i in li:
            result.append(ranks[i])
        return result