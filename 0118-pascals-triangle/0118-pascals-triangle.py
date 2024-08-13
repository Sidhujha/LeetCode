class Solution:
    def pas(self,r,c):
        res=1
        for i in range(c):
            res=res*(r-i)
            res=res//(i+1)
        return res
    def generate(self, numRows: int) -> List[List[int]]:
        li=[]
        for i in range(1,numRows+1):
            lis=[]
            for j in range(1,i+1):
                lis.append(self.pas(i-1,j-1))
            li.append(lis)
        return li
        