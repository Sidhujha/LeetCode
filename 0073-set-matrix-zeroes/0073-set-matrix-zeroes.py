class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        li=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    li.append([i,j])
        for i in li:
            for j in range(len(matrix)):
                for k in range(len(matrix[0])):
                    if j==i[0] or k==i[1]:
                        matrix[j][k]=0
        return matrix