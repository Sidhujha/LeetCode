class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5=0
        c10=0
        res=True
        for i in bills:
            if i==5:
                c5+=1
            if i==10:
                if c5>0:
                    c10+=1
                    c5-=1
                else:
                    res=False
                    break
            if i==20:
                if c5>0 and c10>0:
                    c5-=1
                    c10-=1
                elif c5>2:
                    c5-=3
                else:
                    res=False
                    break
        return res