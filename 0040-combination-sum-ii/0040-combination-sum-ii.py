class Solution:
    def combinationSum2(self, candidates, target):
        def sid(i,n,li,lis,target,res):
            if target==0:
                res.append(list(lis))
                return
            for j in range(i,n):
                if j>i and li[j]==li[j-1]:
                    continue
                if li[j]>target:
                    break
                lis.append(li[j])
                sid(j+1,n,li,lis,target-li[j],res)
                lis.pop()
        candidates.sort()
        ans = []
        ds = []
        sid(0, len(candidates), candidates,ds,target, ans)
        return ans

        