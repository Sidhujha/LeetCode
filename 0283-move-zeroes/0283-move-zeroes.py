class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in arr:
    	    if i==0:
    	        arr.remove(i)
    	        arr.append(i)
        