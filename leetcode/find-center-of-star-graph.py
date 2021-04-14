# find-center-of-star-graph.py
'''
star graph であることが保証されているのであれば、頭の2つを見て共通の値は何かを見ればよい
これもなんでMediumなのかわからないな…この後にディスカッションが続くという意味でのMediumかな？
'''

class Solution:
    def findCenter(self, edges) -> int:
        for i in edges[0]:
            if i in edges[1]:
                return i

testcases = [
    [[1,2],[2,3],[4,2]],
     [[1,2],[5,1],[1,3],[1,4]]
]

for edges in testcases:
    print(Solution().findCenter(edges))