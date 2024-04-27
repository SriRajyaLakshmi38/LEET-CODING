class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def find2min(p):
            min1=min2= maxsize
            for num in grid[p]:
                if num < min1:
                    min2 = min1
                    min1 = num
                elif num < min2:
                    min2 = num
            return min1,min2


        for i in range(n-2,-1,-1):
            min1,min2 = find2min(i+1)
            for j in range(n):
                if grid[i+1][j]==min1:
                    grid[i][j]+=min2
                else:
                    grid[i][j]+=min1
         
        return min(grid[0])