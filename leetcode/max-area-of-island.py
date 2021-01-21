# max-area-of-island.py
'''
基本的な方針としては、for 文で各要素を見ていく。未見かつ島だったら dfs で島を探し出す。
あー、だからしたみたいに書いてるんだ。
return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))
こういう書き方出来るのすごいな、とはいえめっちゃ怖いところも在るけど。
seen を set で管理するの面白かった。確かに set((y,x)) ってしてあげることで seen[y][x] と同じことができる。
どっちもO(1)で取ってくることができるけど、set のほうがちょっと見やすいかも?
'''
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        seen = set()
        def is_out_of_range(x,y):
            if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
                return False
            return True
        def area(x,y):
            if is_out_of_range(x,y) and (x,y) not in seen and grid[y][x]==1:
                seen.add((x,y))
                return 1 + area(x-1, y) + area(x+1, y) + area(x, y-1) + area(x, y+1)
            return 0
        return max(area(x,y) for x in range(len(grid[0])) for y in range(len(grid)))


glid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

sol = Solution().maxAreaOfIsland(glid)
print(sol)

