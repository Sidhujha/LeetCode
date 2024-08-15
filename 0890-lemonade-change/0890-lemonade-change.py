class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        li=[]
        res=True
        for i in bills:
            if i==5:
                li.append(i)
            if i==10:
                if 5 in li:
                    li.append(i)
                    li.remove(5)
                else:
                    res=False
                    break
            if i==20:
                if 5 in li and 10 in li:
                    li.append(i)
                    li.remove(5)
                    li.remove(10)
                elif 5 in li and li.count(5)>2:
                    li.append(i)
                    li.remove(5)
                    li.remove(5)
                    li.remove(5)
                else:
                    res=False
                    break
        return res