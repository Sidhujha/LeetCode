class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        li=[k*i for i in range(1,105)]
        for i in li:
            if (i%k==0 and i not in nums):
                return i