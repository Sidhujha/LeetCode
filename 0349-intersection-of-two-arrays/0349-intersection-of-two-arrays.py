class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li=[]
        s=set(nums2)
        for i in nums1:
            if i in s:
                li.append(i)
        li=list(set(li))
        return li