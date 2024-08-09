class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        c=0
        li=[]
        li=set(li)
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if grid[i][j]>0 and grid[i][j]<10:
                    li.add(grid[i][j])
                if grid[i][j+1]>0 and grid[i][j+1]<10:
                    li.add(grid[i][j+1])
                if grid[i][j+2]>0 and grid[i][j+2]<10:
                    li.add(grid[i][j+2])
                if grid[i+1][j]>0 and grid[i+1][j]<10:
                    li.add(grid[i+1][j])
                if grid[i+1][j+1]>0 and grid[i+1][j+1]<10:
                    li.add(grid[i+1][j+1])
                if grid[i+1][j+2]>0 and grid[i+1][j+2]<10:
                    li.add(grid[i+1][j+2])
                if grid[i+2][j]>0 and grid[i+2][j]<10:
                    li.add(grid[i+2][j])
                if grid[i+2][j+1]>0 and grid[i+2][j+1]<10:
                    li.add(grid[i+2][j+1])
                if grid[i+2][j+2]>0 and grid[i+2][j+2]<10:
                    li.add(grid[i+2][j+2])
                if len(li)==9:
                    if grid[i][j]+grid[i][j+1]+grid[i][j+2]==grid[i][j]+grid[i+1][j]+grid[i+2][j]==grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1]==grid[i+1][j]+grid[i+1][j+1]+grid[i+1][j+2]==grid[i][j+2]+grid[i+1][j+2]+grid[i+2][j+2]==grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]==grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]==grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]:
                        c+=1
                        li=set([])
                else:
                    li=set([])
        return c