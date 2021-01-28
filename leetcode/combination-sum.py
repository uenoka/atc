# combination-sum.py
'''
「候補が何通りあるか」であれば結構単純な動的計画法でいけるが、この場合候補の数字自体も必要になるのでどう実装していくかというのが肝っぽそう。
普通に DFS でいけるっぽい（確かに超えたら return, ちょどになったら答えに入れるをしたらいいっぽい）
それなら単純なBit全探索でもよいかも（というかそれをしなかったのはなんでだっけ…？）
この手の DFS というか再帰、やっぱり苦手だなぁ…
'''
class Solution:
    def combinationSum(self, candidates, target: int) :
        def dfs(candidates,target,ret):
            for i in candidates:
                ret.append(i)
                if sum(ret)<=target:
                    dfs(candidates,target,ret)
            return  ret
        return dfs(candidates,target,[])

    def kb_combinationSum(self, candidates, target: int) :
        dp = [[0]*(target+1) for _ in range(len(candidates)+1)]
        for i in range(1,len(candidates)+1):
            for j in range(1,target+1):
                if j%candidates[i-1]==0:
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-candidates[i-1]]
        return dp[len(candidates)][target]




sol = Solution()
candidates = [2,3,4,7]
target = 7
print(sol.combinationSum(candidates,target))