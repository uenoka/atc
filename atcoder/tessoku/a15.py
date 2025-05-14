'''

# 問題概要

与えられた配列の大小関係を圧縮する。

# 例

input : 46 80 11 77 46
output : 2 4 1 3 2

# 考察

愚直にやるなら入力の配列を2重ループして何個目に大きいかをチェック→回答に追加、とやるのが良い
```
N = input()
A = list(map(int,input().split()))
ans = []
B = list(set(A))
for a in A:
    idx = 1
    for b in B:
        if b < a:
            idx += 1
    ans.append(idx)
print(ans)
```
このときAを一意にしといたほうが楽なのでBを作る。
計算量は O(N**2)

そうするとBをソートして、2分探索して上げる方法も良さそうに見えてくる
```
import bisect
N = input()
A = list(map(int,input().split()))
ans = []
B = sorted(list(set(A)))
for a in A:
    ans.append(bisect.bisect_right(B,a))
print(*ans)
```
こうすると計算量は O(NlogN)。N<10**5 なので十分高速
'''

import bisect
N = input()
A = list(map(int,input().split()))
ans = []
B = sorted(list(set(A)))
for a in A:
    ans.append(bisect.bisect_right(B,a))
print(*ans)
