# decode-xored-array.py
'''
xor の操作を知っているか？や基本的な操作を知っているか等の問題
A xor B = B xor A
A xor B xor B = A
ここら辺のよくみる性質を知っているとよい
10 での xor 自体が「同じ場合 0 違う場合 1 」だから
同じ数同士の xor = 0 を作り出す -> 0 との xor は変化しないから、
それはそうって感じだけど毎度この性質を実験したりでやるのは面倒。。。
'''

class Solution:
    def decode(self, encoded, first: int):
        ans = [first]
        idx = 0
        for i in encoded:
            ans.append(ans[idx]^i)
            idx += 1
        return ans

testcases = [
    [[1, 2, 3], 1],
    [[6, 2, 7, 3], 4],
]

for encoded, first in testcases:
    sol = Solution().decode(encoded, first)
    print(sol)
