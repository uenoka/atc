# minimum-number-of-vertices-to-reach-all-nodes.py
'''
どこからも参照されていないノードの数が最小値のはず -> これをどう証明するか。
一応O(N)だが、87.95% fasterなのでもう少し高速化できそう。どうするか？
'''
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        all_nodes = set([i for i in range(n)])
        for node in edges:
            if node[1] in all_nodes:
                all_nodes.remove(node[1])
        return all_nodes

testcases = [
    [6,[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]],
    [5,[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]]
]
for n,edges in testcases:
    sol = Solution().findSmallestSetOfVertices(n, edges)
    print(sol)
