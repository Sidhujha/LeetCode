class Solution:
    def numIslands(self, li: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=len(li) or j<0 or j>=len(li[0]) or li[i][j]=="0":
                return
            li[i][j]="0"
            for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(i+x,j+y)
        c=0
        for i in range(len(li)):
            for j in range(len(li[0])):
                if li[i][j]=="1":
                    dfs(i,j)  
                    c+=1
        return c