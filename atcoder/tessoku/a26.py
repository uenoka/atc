'''
# 問題

以下の $Q$ 個の質問に答えるプログラムを作成してください。

* 質問 $1$ ：整数 $X\_1$ は素数ですか？
* 質問 $2$ ：整数 $X\_2$ は素数ですか？
* 質問 $3$ ：整数 $X\_3$ は素数ですか？
* $\dots$
* 質問 $Q$ ：整数 $X\_Q$ は素数ですか？

# 考察
素数判定。
√N まで求めればいい。今回の場合、もしかしたらキャッシュ残してあげるともうちょっと高速化出来るかも?
'''
import math
cache = {}
def is_prime(x):
    if x in cache:
        return cache[x]
    is_prime = True
    for i in range (2, int(math.sqrt(x)) + 1):
        is_prime = x%i != 0
        if not is_prime:
            break
    if is_prime:
        cache[x] = 'Yes'
    else:
        cache[x] = 'No'
    return cache[x]
N = int(input())
for _ in range(N):
    x = int(input())
    print(is_prime(x))