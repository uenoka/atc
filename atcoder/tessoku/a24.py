'''
# 問題

配列 $A = \[A\_1, A\_2, \cdots, A\_N]$ の最長増加部分列の長さを求めてください。

# 問題概要

最長増加部分列の問題

# 入力例

6
2 3 1 6 4 5
-> 4(2,3,4,5 を選ぶと最長になる)

# 考察
パッと見は簡単そう、i 番目のときの LIS は i-1 番目までの LIS から増加しているかどうか、という感じで考えたが
ふと増加しているとかそういうのが意外に難しいことに気づく。
'''
from bisect import bisect_left
def lis_length(A):
    dp = []
    for a in A:
        pos = bisect_left(dp, a)
        if pos == len(dp):
            dp.append(a)
        else:
            dp[pos] = a
    return len(dp)
# 入力
N = int(input())
A = list(map(int,input().split()))

result = lis_length(A)
print(result)
