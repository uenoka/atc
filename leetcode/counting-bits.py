# counting-bits.py
'''
普通に変換→それぞれの値で1を数える、という方法であればすぐできるが、これだと重い（通りはするが）
同じような方法で高速化するにはメモ化ができそう？(5 = 1 + 4 なので4と1をメモしておけばO(1)で取得できる。同様に9 = 5 + 4 = 4 + 4 + 1 みたいな形でとってこれる)
いや、でもこれ結局2進数変換するのと同じことしてるからもっといい方法がありそう…
O(nlogn) 解法がBit操作。O(N)はDP（メモ化）なのでまぁ間違ってはなかった。
bit 操作の「N を2進数で表したときにK個の1があるとき、N&(N-1)にはK-1個の1がある」
例：N=7 の場合
7 = 111 -> 3個の1
6 = 110 -> 2個の1
7&6 = 110 = 6
5 = 101 -> 2個の1
6&5 = 100 = 4
4 = 100
4 & 3 = 0
==
どういう性質か、どう証明するかまではよくわからないが、この操作をするとNを超えない最大の2の累乗の数に最後は到達する。
'''
from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        def first_sol(num):
            ans = []
            for i in range(num+1):
                binary = bin(i)
                str_bin = str(binary)[2:]
                ans.append(str_bin.count("1"))
            return ans

        def bit_sol(num):
            ans = []
            for i in range(num+1):
                tmp = i
                cnt = 0
                print('===== n',i)
                while tmp>0:
                    print(tmp,tmp&(tmp-1))
                    tmp &= tmp-1
                    cnt += 1
                ans.append(cnt)
            return ans

        def dp_sol(num):
            ans = []
            return ans
        return bit_sol(num)
testcases = [
    # 30
]
for num in testcases:
    sol = Solution().countBits(num)
    print(sol)
