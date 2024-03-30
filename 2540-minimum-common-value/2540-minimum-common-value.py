class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        inter=set(nums1).intersection(set(nums2))
        return min(inter) if len(inter)>0  else -1 