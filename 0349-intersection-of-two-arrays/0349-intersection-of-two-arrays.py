class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li=[]
        for i in nums1:
            if i in nums2:
                li.append(i)
        li=list(set(li))
        return li