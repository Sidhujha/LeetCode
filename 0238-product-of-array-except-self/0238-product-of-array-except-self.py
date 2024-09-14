class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pr=1
        sr=1
        pa=[]
        sa=[]
        pa.append(pr)
        sa.append(sr)
        for i in nums[:-1]:
            m=i*pr
            pr=m
            pa.append(m)
        for i in nums[:0:-1]:
            m=i*sr
            sr=m
            sa.append(m)
        sa=sa[::-1]
        res=[]
        for i in range(len(nums)):
            res.append(pa[i]*sa[i])
        return res