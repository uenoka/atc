# island-perimeter.py
'''
grid 上のやつなので BFS で解いてみた。
ただ、速度もメモリもかなり遅めなのが気になる。
'''


class Solution:

    def islandPerimeter(self, grid) -> int:
        import queue
        queue = queue.Queue()
        seen = [[False]*len(grid[0]) for _ in range(len(grid))]
        flg = False
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    sc = j
                    sr = i
                    flg = True
            if flg:
                break
        queue.put((sr, sc))
        seen[sr][sc] = True
        ans = 0
        while not queue.empty():
            y, x = queue.get()
            cnt = 0
            for i in range(4):
                if self.can_go(y, x, dy[i], dx[i], grid):
                    cnt += 1
                    if self.is_seen(y, x, dy[i], dx[i], seen):
                        queue.put((y+dy[i], x+dx[i]))
                        seen[y+dy[i]][x+dx[i]] = True
            print(y, x)
            ans += 4-cnt
        return ans

    def can_go(self, y, x, dy, dx, grid):
        if y+dy >= len(grid) or x+dx >= len(grid[0]) or x+dx < 0 or y+dy < 0:
            return False
        if grid[y+dy][x+dx] == 0:
            return False
        return True

    def is_seen(self, y, x, dy, dx, seen):
        if seen[y+dy][x+dx]:
            return False
        return True


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
# grid = [[1]]
# grid = [[1, 1]]
sol = Solution()
print(sol.islandPerimeter(grid))
