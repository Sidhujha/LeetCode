class Solution:
    def generate(self, n: int) -> List[List[int]]:
        li=[]
        for i in range(1,n+1):
            ans=1
            lis=[]
            lis.append(1)
            for j in range(1,i):
                ans=ans*(i-j)
                ans=ans//j
                lis.append(ans)
            li.append(lis)
        return li