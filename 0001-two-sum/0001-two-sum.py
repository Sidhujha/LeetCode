class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li=sorted(nums)
        i=0
        j=len(nums)-1
        while(i<j):
            if li[i]+li[j]>target:
                j-=1
            elif li[i]+li[j]==target:
                break
            else:
                i+=1
        res=[]
        for k in range(len(nums)):
            if li[i]==nums[k]:
                res.append(k)
                break
        for k in range(len(nums)-1,-1,-1):
            if li[j]==nums[k]:
                res.append(k)
                break
        return res
