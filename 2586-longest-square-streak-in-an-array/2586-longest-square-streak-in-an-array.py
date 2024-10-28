class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        maxcount=1
        while(nums):
            i= nums.pop()
            count=1
            sq= i**2
            sqroot = math.sqrt(i)
            while(sq in nums):
                count+=1
                nums.remove(sq)
                sq=sq**2
            while (sqroot in nums):
                count+=1
                nums.remove(sqroot)
                sqroot = math.sqrt(sqroot)
            if count==5: return count
            elif count>maxcount:
                maxcount= count        
        return maxcount if maxcount>1 else -1       