# check-array-formation-through-concatenation.py
'''
You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct.
Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].
Return true if it is possible to form the array arr from pieces. Otherwise, return false.
解説AC
↓ の解法頭いいなぁ、arr, pieces を以下につき合わせるかじゃなくて pieces から arr を構築できるかというのをものすごくうまく実装してる。
ただこの解法は、みんな同じようにやってるO(N)解法だから、有名回答なのかも。
O(N)ではなくてO(N+M)が正しそうだけど。
愚直にやろうとするとO(NM)になる。
'''


class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        mp = {x[0]: x for x in pieces}
        res = []
        for num in arr:
            tmp = mp.get(num, [])
            res += tmp
        print(res)
        print(arr)
        return res == arr


sol = Solution()
# arr = [15, 88]
# pieces = [[88], [15]]
arr = [49, 18, 16]
pieces = [[16, 18, 49]]

print(sol.canFormArray(arr, pieces))
