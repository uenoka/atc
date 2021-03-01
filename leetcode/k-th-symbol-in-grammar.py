# k-th-symbol-in-grammar.py
'''
とりあえず再帰で書いてみた。これをビット演算でどうにかreverseをO(1)でかければよさそう
-> 色々な解法を見た感じ、K が 2^N / 2 より大きいか小さいかで場合分けするパターン（これだとO(logN)でできる）と
01 の表示のされ方が K-1 の2進法での1の出現の偶奇と一致することを利用する O(1) のパターンがある。
正直後者は思い浮かばないのと、そもそも偶然この設問で一致するだけでこの設問との関連性はなさそうなので、出来るようになるのは前者。
なるほど確かに半分にしていってとやっていけばだんだんと範囲が狭まるのが面白い。
'''
import sys
sys.setrecursionlimit(500000)
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N==1 and K == 1:
            return 0
        mid = (2**(N-1))//2
        if K <= mid:
            return self.kthGrammar(N-1, K)
        else:
            return int(not self.kthGrammar(N-1, K-mid))


testcases = [
    # (1, 1),
    # (2, 2),
    # (3, 3),
    (4, 3),
    (5, 3),
    # (25, 1),
    # (30, 1),
    # (30, 10),
    # (30, 100),
    # (30, 1000),
    # (30, 10000),
    # (30, 2),
    # (30, 3)
]

for N,K in testcases:
    sol = Solution().kthGrammar(N,K)
    print(sol)
