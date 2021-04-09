# number-of-islands.py
class Solution:
    def numIslands(self, grid) -> int:
        import sys
        sys.setrecursionlimit(500000)
        H = len(grid)
        W = len(grid[0])
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        seen = [[False] * W for i in range(H)]
        # 島なら8方向、迷路なら4方向などの行先判定
        def canGo(nh,nw,i,j):
            if i==0 and j==0:return False
            if (i==1 or i==-1) and (j==1 or j==-1) : return False
            if nh < 0 or nw < 0 or nh >= H or nw >= W : return False
            if seen[nh][nw] : return False
            if grid[nh][nw] == '0' : return False
            return True
        def dsf(h,w):
            seen[h][w] =True
            for i in range(4):
                nh = h + dx[i]
                nw = w + dy[i]
                if canGo(nh,nw,dx[i],dy[i]):
                    dsf(nh,nw)
        def printseen():
            print('=======')
            for i in seen:
                print(i)
            print('=======')
        ans = 0
        for row_idx,row in enumerate(grid):
            for col_idx,col in enumerate(row):
                if grid[row_idx][col_idx]=='1' and not seen[row_idx][col_idx]:
                    ans += 1
                    dsf(row_idx,col_idx)
            # printseen()
        return ans


sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))