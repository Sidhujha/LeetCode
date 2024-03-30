class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        inter=set(nums1).intersection(set(nums2))
        return min(inter) if len(inter)>0  else -1 