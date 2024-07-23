class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li=[]
        for i in range(len(nums)):
            s=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==s:
                    li.extend([i,j])
        return li
