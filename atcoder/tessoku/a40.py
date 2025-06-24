
'''
# 問題

机の上に $N$ 本の棒が置かれています。 左から $i$ 番目の棒（棒 $i$ とする）の長さは $A\_i$ メートルです。

$3$ つの異なる棒を選んで**正三角形**を作る方法は何通りありますか。

# 考察

同じ長さでグルーピングして、それぞれで nCr する。

'''
N = int(input())
A = list(map(int,input().split()))
from collections import Counter
sides = Counter(A)
ans = 0
for _,i in sides.items():
    tmp = 1
    if i < 3:
        continue
    for j in range(3):
        tmp = tmp * (i-j) // (j+1) 
    ans += tmp
print(ans)