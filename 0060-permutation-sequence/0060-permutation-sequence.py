class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac=1
        li=[]
        for i in range(1,n):
            fac*=i
            li.append(i)
        li.append(n)
        k=k-1
        ans=""
        while True:
            a=li[k//fac]
            ans=ans+str(a)
            li.remove(a)
            if len(li)==0:
                break
            k=k%fac
            fac=fac//len(li)
        return ans
