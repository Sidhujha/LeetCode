class Solution:
    def perm(self,ind,li,res,k):
        if len(res)==k+35000:
            return
        if ind==len(li):
            res.append(list(li))
            return
        for i in range(ind,len(li)):
            li[i],li[ind]=li[ind],li[i]
            self.perm(ind+1,li,res,k)
            li[i],li[ind]=li[ind],li[i]
    def getPermutation(self, n: int, k: int) -> str:
        li=[]
        res=[]
        for i in range(1,n+1):
            li.append(i)
        self.perm(0,li,res,k)
        res.sort()
        ans=""
        for i in res[k-1]:
            ans+=str(i)
        return ans