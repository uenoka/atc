# sort-the-matrix-diagonally.py
'''
・斜めを配列に入れてすべて入れてそれぞれソート→再構築で行く？
・インデックスを管理してそれぞれIn-placeでソートする？
どちらにせよかなり大変だな…
ちょっと厳しいのでいったんどうやってるのか解説見て読み解く
'''
class Solution:
    def diagonalSort(self, mat):
        for i in range(len(mat[0])):
            temp=[]
            temp.append(mat[0][i])
            for j in range(1,len(mat)):
                if i+j < len(mat[0]):
                    temp.append(mat[j][i+j])
            temp.sort()
            for j in range(len(temp)):
                mat[j][i+j]=temp[j]
        for i in range(1,len(mat)):
            temp=[]
            temp.append(mat[i][0])
            for j in range(1,len(mat[0])):
                if i+j < len(mat):
                    temp.append(mat[i+j][j])
            temp.sort()
            for j in range(len(temp)):
                mat[i+j][j]=temp[j]
        return mat


testcases = [
    [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
]
for mat in testcases:
    sol = Solution().diagonalSort(mat)
    print(sol)

