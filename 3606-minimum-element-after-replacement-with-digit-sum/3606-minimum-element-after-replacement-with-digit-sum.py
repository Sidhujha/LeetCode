class Solution:
    def minElement(self, nums: List[int]) -> int:
        li=[]
        for i in nums:
            s=0
            for j in str(i):
                s+=int(j)
            li.append(s)
        return min(li)