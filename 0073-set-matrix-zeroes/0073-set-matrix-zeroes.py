class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a=[0]*len(matrix)
        b=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    a[i]=1
                    b[j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if a[i]==1 or b[j]==1:
                    matrix[i][j]=0
        return matrix