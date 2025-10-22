class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        li=[]
        for i in nums:
            if i not in li:
                if nums.count(i)%k==0:
                    for j in range(nums.count(i)):
                        li.append(i)
        return sum(li)