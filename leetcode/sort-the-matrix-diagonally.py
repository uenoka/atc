# sort-the-matrix-diagonally.py
'''
・斜めを配列に入れてすべて入れてそれぞれソート→再構築で行く？
・インデックスを管理してそれぞれIn-placeでソートする？
どちらにせよかなり大変だな…
'''
class Solution:
    def diagonalSort(self, mat):
        return []

testcases = [
    [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
]
for mat in testcases:
    sol = Solution().diagonalSort(mat)
    print(sol)

